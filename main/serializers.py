from rest_framework.serializers import ModelSerializer
from main.models import Category, Company, Product, User


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
