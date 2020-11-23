from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from rooms.models import Room, RoomPhoto
from users.models import User
from django_seed import Seed
from faker import Faker
import random
import os

titles = [
    '매일 농구 인증',
    '캠핑 상자',
    '일주일에 5일 운동하기',
    '만보 걷기',
    '매일 10분 악기, 노래 연습',
    '달리기, 마라톤',
    '매일 10k 러닝 인증',
    '다이어트(독하게 살뺄 사람만)',
    '매일매일 조금씩 독서 인증',
    '크리오 타는 사람들',
    '나무 젓가락 공예',
    '하루에 영단어 하나씩 외우기',
    '매일 우리 역시 알아보기',
    '유튜브 함께만들고 함께 성장하는 유튜버 모임',
    '매일 사전 베끼기',
    '그리다 만들다',
    '하루 오천보 걷기 인증',
    '운동일지',
    '삼시세끼 요리하고 인증',
    '시사 인증',
    '하루 푸쉬업 100회하기'
]
room_photo_filenames = os.listdir('./uploads/rooms')
all_users = User.objects.all()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--times', type=int, help='how many times?')

    def handle(self, *args, **options):
        times = options.get('times')
        seeder = Seed.seeder()

        seeder.add_entity(Room, times, {
            'title': lambda x: random.choice(titles),
            'description' : lambda x: seeder.faker.text(),
            'host': lambda x: random.choice(all_users),
        })
        created_rooms = seeder.execute()
        created_clean = flatten(list(created_rooms.values()))
        for pk in created_clean:
            room = Room.objects.get(pk=pk)
            for i in range(3, random.randint(5, 10)):
                RoomPhoto.objects.create(
                    file = f'rooms/{random.choice(room_photo_filenames)}',
                    caption = seeder.faker.sentence(),
                    room=room
                )