# Generated by Django 3.1.4 on 2021-01-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20201229_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=200)),
            ],
        ),
    ]
