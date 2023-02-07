from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import ProductSerializer
from .models import Product
from rest_framework.parsers import JSONParser
from rest_framework import views, viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin


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


class ProductViewSet(
        DestroyModelMixin,
        ListModelMixin,
        RetrieveModelMixin, 
        viewsets.GenericViewSet,
        UpdateModelMixin
        ):
    """
    A simple ViewSet for listing, retrieving, deleting or updating products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
















    


