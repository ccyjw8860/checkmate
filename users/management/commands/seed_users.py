from django.core.management.base import BaseCommand
from users.models import User
from django_seed import Seed

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, help='how many times?')

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, int(number), {
            'is_staff':False,
            'is_superuser':False
        })
        seeder.execute()