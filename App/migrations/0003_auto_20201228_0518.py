# Generated by Django 3.1.4 on 2020-12-27 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
