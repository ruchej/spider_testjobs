from django.db import models
from django.contrib.auth.models import AbstractUser


class IsActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class MainProp(models.Model):
    """Основные свойства"""

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=1000, blank=True, null=True,
                                   verbose_name='Описание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Объект активен')
    objects = models.Manager()
    active = IsActiveManager()

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title
    
    def delete(self, **kwargs):
        if "force" in kwargs:
            super().delete()
        else:
            self.is_active = False
            self.save()


class Category(MainProp):
    """Категории"""

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class IntegrateCompanyManager(models.Manager):
    """Возвращает только интегрированные компании"""
    def get_queryset(self):
        return super().get_queryset().filter(id_external__isnull=False)


class Company(MainProp):
    """Компании"""

    id_external = models.PositiveIntegerField(blank=True, null=True, verbose_name='Внешний id компании')
    objects = models.Manager()
    integrated = IntegrateCompanyManager()

    class Meta:

        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Product(MainProp):
    """Продукция"""

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')
    id_prod_comp = models.PositiveIntegerField(blank=True, null=True, db_index=True, verbose_name='id продукта у поставщика')

    class Meta:

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'


class User(AbstractUser):
    """Пользователи"""

    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')

    class Meta:

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
