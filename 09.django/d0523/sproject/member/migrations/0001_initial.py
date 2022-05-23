# Generated by Django 4.0.4 on 2022-05-23 01:21

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
                ('address1', models.CharField(blank=True, max_length=300)),
                ('address2', models.CharField(blank=True, max_length=300)),
                ('gender', models.CharField(default='남자', max_length=10)),
                ('hobby', models.CharField(blank=True, max_length=100)),
                ('creatdate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 10, 21, 50, 627915))),
                ('updatedate', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 10, 21, 50, 627915))),
            ],
        ),
    ]
