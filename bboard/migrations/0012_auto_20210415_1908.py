# Generated by Django 3.1.7 on 2021-04-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0011_auto_20210407_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
