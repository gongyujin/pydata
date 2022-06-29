# Generated by Django 4.0.4 on 2022-06-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0008_alter_members_user_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='user_target',
            field=models.CharField(choices=[('Abs', '복부'), ('Shoulders', '어깨'), ('Arms', '팔'), ('Back', '등'), ('Chest', '가슴'), ('Legs', '하체'), ('All', '전신')], max_length=1000, null=True),
        ),
    ]