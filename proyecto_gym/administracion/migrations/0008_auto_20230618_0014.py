# Generated by Django 3.2.18 on 2023-06-18 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_alter_grupo_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='numero',
        ),
        migrations.AddField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(default='Sin nombre', max_length=100, verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]
