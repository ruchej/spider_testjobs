from django.contrib import admin
from main.models import Category, Company, Product, User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
   list_display = ('title', 'id_external') 
   list_filter = (
       ('id_external', admin.EmptyFieldListFilter),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

