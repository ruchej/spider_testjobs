from django.urls import path, include
from rest_framework import routers

from main.api import CategoryViewSet, CompanyViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register('categorys', CategoryViewSet)
router.register('companys', CompanyViewSet)
router.register('products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]