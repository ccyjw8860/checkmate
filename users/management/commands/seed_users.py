from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from users.models import User
from rooms.models import Room
from django_seed import Seed
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--times', default=1, type=int, help='how many times?')

    def handle(self, *args, **options):
        number = options.get('times')
        rooms = Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            'is_staff':False,
            'is_superuser':False
        })
        created_users = seeder.execute()
        created_cleaned = flatten(list(created_users.values()))
        for pk in created_cleaned:
            user = User.objects.get(pk=pk)
            howmany = random.randint(0, 5)
            if howmany > 0:
                for i in range(howmany):
                    room = random.choice(rooms)
                    user.rooms.add(room)









