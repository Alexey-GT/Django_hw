from django.core.management.base import BaseCommand
from homework2_app.models import User, Product


class Command(BaseCommand):
    help = "Get all product by user id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            product = Product.objects.filter(user=user)
            intro = f'All product of {user.name}\n'
            text = '\n'.join(product.name for prod in product)
            self.stdout.write(f'{intro}{text}')
