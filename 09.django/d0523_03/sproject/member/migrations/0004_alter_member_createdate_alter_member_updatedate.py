# Generated by Django 4.0.4 on 2022-05-23 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_createdate_alter_member_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='createdate',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 23, 10, 59, 30, 394470)),
        ),
        migrations.AlterField(
            model_name='member',
            name='updatedate',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 23, 10, 59, 30, 394470)),
        ),
    ]