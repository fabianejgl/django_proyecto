# Generated by Django 3.2.18 on 2023-06-17 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_auto_20230613_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='nombre',
        ),
        migrations.AddField(
            model_name='grupo',
            name='numero',
            field=models.IntegerField(default=0, verbose_name='numero'),
        ),
    ]