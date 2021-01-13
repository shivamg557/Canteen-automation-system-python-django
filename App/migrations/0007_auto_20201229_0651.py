# Generated by Django 3.1.4 on 2020-12-29 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_userprofileinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='password1',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='password2',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
