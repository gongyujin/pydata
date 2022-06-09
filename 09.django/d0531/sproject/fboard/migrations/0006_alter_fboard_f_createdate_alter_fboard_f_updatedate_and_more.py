# Generated by Django 4.0.4 on 2022-05-30 01:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_alter_member_createdate_alter_member_updatedate'),
        ('fboard', '0005_alter_fboard_f_createdate_alter_fboard_f_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='f_createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 30, 10, 45, 18, 853172)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='f_updatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 30, 10, 45, 18, 853172)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('c_no', models.AutoField(primary_key=True, serialize=False)),
                ('c_pw', models.CharField(blank=True, max_length=100)),
                ('c_content', models.TextField()),
                ('c_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 30, 10, 45, 18, 854164))),
                ('fboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fboard.fboard')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]