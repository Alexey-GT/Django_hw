from django.core.management.base import BaseCommand
from homework2_app.models import User, Product, Order


class Command(BaseCommand):
    help = "Adding data to a table"

    def handle(self, *args, **kwargs):
        user = User(name='Alex', email='Alex@example.com',
                    phone_number='8-908-1234567', client_address="I'm here and I'm everywhere", )
        user.save()
        product = Product(name="Bicycle", description="Something interesting", price=1000.24,
                          quantity=43, )
        product.save()

        self.stdout.write(f'{user}')
        self.stdout.write(f'{product}')
