from django.urls import path
from django.contrib import admin
from core import views as core_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'productlisting', core_views.ProductViewSet, basename='product')



urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('product/', core_views.ProductAPIView.as_view()),
    path('api-token-auth/',obtain_auth_token)

]