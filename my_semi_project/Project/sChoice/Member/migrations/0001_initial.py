# Generated by Django 4.0.4 on 2022-06-07 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('pro', models.IntegerField(default=0)),
                ('birth', models.DateField(blank=True)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('phone', models.CharField(blank=True, max_length=13)),
                ('zipcode', models.CharField(blank=True, max_length=6)),
                ('addressd1', models.CharField(blank=True, max_length=1000)),
                ('addressd2', models.CharField(blank=True, max_length=1000)),
                ('user_purpose', models.CharField(blank=True, max_length=1000)),
                ('service', models.CharField(blank=True, max_length=1000)),
                ('vegan', models.IntegerField(default=0)),
                ('allergic_food', models.CharField(blank=True, max_length=1000)),
                ('goal_wieght', models.IntegerField(default=55)),
                ('goal_bodyfat', models.IntegerField(default=25)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('modidate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dailydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(blank=True)),
                ('cur_weight', models.IntegerField(blank=True)),
                ('cur_bodyfat', models.IntegerField(blank=True)),
                ('cur_neck', models.IntegerField(blank=True)),
                ('cur_waist', models.IntegerField(blank=True)),
                ('cur_hip', models.IntegerField(blank=True)),
                ('day_img', models.ImageField(blank=True, upload_to='')),
                ('ex_level', models.CharField(blank=True, max_length=100)),
                ('week_ex', models.IntegerField(default=0)),
                ('day_ex', models.IntegerField(default=0)),
                ('focus_ex', models.CharField(blank=True, max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Member.members')),
            ],
        ),
    ]
