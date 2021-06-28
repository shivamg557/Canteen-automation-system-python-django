# Generated by Django 3.1.4 on 2021-05-31 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_auto_20210526_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateTimeField(auto_now_add=True)),
                ('recieve_date', models.DateField()),
                ('recieve_time', models.TimeField()),
                ('pay_status', models.BooleanField(default=False)),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.orderitem')),
            ],
        ),
    ]