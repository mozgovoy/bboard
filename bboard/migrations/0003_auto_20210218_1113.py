# Generated by Django 3.1.4 on 2021-02-18 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20210218_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Рубрика'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Никнейм'),
        ),
    ]