import requests
import json

from django.core.management.base import BaseCommand, CommandError

from main.models import Category, Company, Product, User


class Command(BaseCommand):
    help = 'Синхронизация данных с удалённым ресурсом'

    def handle(self, *args, **options):
        base_url = 'http://otp.spider.ru/test/companies/'
        product_add_url = 'localhost://api/products/'
        integrated_companys = Company.integrated.all()
        for company in integrated_companys:
            url = f'{base_url}/{company.pk}/products'
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.content.decode('utf-8'))
                response = requests.post(url, data=data)
                self.stdout.write(self.style.SUCCESS(response.status_code))


