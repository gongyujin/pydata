# Generated by Django 4.0.4 on 2022-05-23 01:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_member_creatdate_alter_member_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='creatdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 10, 58, 46, 943169)),
        ),
        migrations.AlterField(
            model_name='member',
            name='updatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 23, 10, 58, 46, 943169)),
        ),
    ]
