# Generated by Django 3.1.7 on 2021-05-30 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_auto_20210531_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(default='2021-01-01'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Персонал'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Супер-пользователь'),
        ),
    ]
