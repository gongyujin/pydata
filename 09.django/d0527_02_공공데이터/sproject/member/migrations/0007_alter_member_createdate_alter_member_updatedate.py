# Generated by Django 4.0.4 on 2022-05-27 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_member_createdate_alter_member_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='createdate',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 27, 17, 17, 37, 503221)),
        ),
        migrations.AlterField(
            model_name='member',
            name='updatedate',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 27, 17, 17, 37, 503221)),
        ),
    ]
