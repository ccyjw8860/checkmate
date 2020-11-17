# Generated by Django 2.2.5 on 2020-11-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(default='')),
                ('file', models.ImageField(upload_to='evidence_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('start_date', models.DateField(default=False)),
                ('end_date', models.DateField(default=False)),
                ('is_group', models.BooleanField(default=False)),
                ('evidence_text', models.CharField(max_length=300)),
            ],
        ),
    ]