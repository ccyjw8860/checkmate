from users.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--times', default=1, type=int, help='how many times?')

    def handle(self, *args, **options):
        number = options.get('times')
        user = User.objects.get(username='yjw8860')
        print(user.username)
        print(user.email)
        print(user.rooms)


