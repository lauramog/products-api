from . models import Product
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.
class ProductTestCase(APITestCase):

    """
    Test suite for Product
    """
    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Product name",
            "detail": "This is a test message",
                    }
        self.url = "/product/"

    def test_create_product(self):
        '''
        test ContactViewSet create method
        '''
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, "Product name")

    def test_create_product_without_name(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_product_when_name_equals_blank(self):
        '''
        test ContactViewSet create method when name is blank
        '''
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_detail(self):
        '''
        test ContactViewSet create method when detail is not in data
        '''
        data = self.data
        data.pop("detail")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_detail_equals_blank(self):
        '''
        test ContactViewSet create method when detail is blank
        '''
        data = self.data
        data["detail"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    