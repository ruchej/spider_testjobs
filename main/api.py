from rest_framework import viewsets
from main.models import Category, Company, Product, User
from main.serializers import CategorySerializer, CompanySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Возвращает все активные категории"""

    queryset = Category.active.all()
    serializer_class = CategorySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """Возвращает все активные категории"""

    queryset = Company.active.all()
    serializer_class = CompanySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Возвращает все активные категории"""

    queryset = Product.active.all()
    serializer_class = ProductSerializer