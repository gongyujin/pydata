# Generated by Django 4.0.4 on 2022-05-25 01:26

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
                ('pw', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('tel', models.CharField(blank=True, max_length=13)),
                ('zipcode', models.CharField(blank=True, max_length=6)),
                ('adress1', models.CharField(blank=True, max_length=300)),
                ('adress2', models.CharField(blank=True, max_length=300)),
                ('gender', models.CharField(default='남자', max_length=10)),
                ('hobby', models.CharField(blank=True, max_length=100)),
                ('createdate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 10, 26, 4, 29911))),
                ('updatedate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 10, 26, 4, 29911))),
            ],
        ),
    ]
