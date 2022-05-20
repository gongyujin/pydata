# Generated by Django 4.0.4 on 2022-05-20 03:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=13)),
                ('zipcode', models.CharField(max_length=6)),
                ('address1', models.CharField(max_length=300)),
                ('address2', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=10)),
                ('hobby', models.CharField(max_length=100)),
                ('creatdate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 20, 12, 14, 28, 420458))),
                ('updatedate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 20, 12, 14, 28, 420458))),
            ],
        ),
    ]