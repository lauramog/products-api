from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import ProductSerializer
from .models import Product
from rest_framework.parsers import JSONParser
from rest_framework import views, viewsets, status
from rest_framework.response import Response


# Create your views here.

class ProductAPIView(views.APIView):
    """
    A simple APIView for creating product entries.
    """
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ProductSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)



    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)







class ProductDetailView(views.APIView):

    def get(self,request,pk,format=None):
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(product)
        try:
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404


    def delete(self,request, pk, format=None):
        product=Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def patch(self,request, pk, format=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product,data=JSONParser().parse(request),partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)






















    


