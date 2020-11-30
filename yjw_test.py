from users.models import User

user = User.objects.get(username='yjw8860')
print(user)


