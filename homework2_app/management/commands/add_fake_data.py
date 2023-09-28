from django.core.management.base import BaseCommand
from homework2_app.models import User, Product


class Command(BaseCommand):
    help = "Generate fake user and product."

    def add_arguments(self, parser):
        parser.add_argument('count_user', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count_user = kwargs.get('count_user')
        for i in range(1, count_user + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@ex.com', phone_number='8-908-1234567',
                        client_address="I'm here and I'm everywhere",)
            user.save()
            for j in range(1, count_user + 1):
                product = Product(name=f'Bicycle{j}', description="Something interesting", price=1000.24 + j ** 2,
                                  quantity=43 - j, )

                product.save()
