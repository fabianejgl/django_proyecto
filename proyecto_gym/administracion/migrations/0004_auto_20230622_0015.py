# Generated by Django 3.2.18 on 2023-06-22 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_sucursal_iframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='iframe',
            field=models.CharField(max_length=1000, verbose_name='Script para iframe'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='link',
            field=models.CharField(max_length=1000, verbose_name='Enlace de Maps'),
        ),
    ]