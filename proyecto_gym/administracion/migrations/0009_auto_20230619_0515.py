# Generated by Django 3.2.18 on 2023-06-19 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_auto_20230618_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inscripcion',
            options={'verbose_name_plural': 'Inscripciones'},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name_plural': 'Profesores'},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={'verbose_name_plural': 'Sucursales'},
        ),
    ]
