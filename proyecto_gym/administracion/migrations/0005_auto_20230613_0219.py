# Generated by Django 3.2.18 on 2023-06-13 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('administracion', '0004_auto_20230602_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('domicilio', models.CharField(max_length=20, verbose_name='Domicilio')),
                ('foto', models.ImageField(null=True, upload_to='perfiles/', verbose_name='Foto Perfil')),
            ],
        ),
        migrations.AlterField(
            model_name='grupo',
            name='dia',
            field=models.IntegerField(choices=[(0, '¡SELECCIONE EL DÍA!'), (1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado')], default=0),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='portada',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Portada'),
        ),
    ]
