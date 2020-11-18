from django.core.management.base import BaseCommand
from rooms.models import Room

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--times', help='how many times?')

    def handle(self, *args, **options):
        times = options.get('times')
        for t in range(int(times)):
            print('i love you')
