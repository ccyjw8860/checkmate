# Generated by Django 2.2.5 on 2020-11-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201123_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rooms',
            field=models.ManyToManyField(related_name='users', to='rooms.Room'),
        ),
    ]
