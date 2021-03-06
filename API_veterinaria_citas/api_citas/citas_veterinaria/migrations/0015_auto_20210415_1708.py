# Generated by Django 3.1.7 on 2021-04-15 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas_veterinaria', '0014_merge_20210415_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascotamodel',
            name='cita',
        ),
        migrations.RemoveField(
            model_name='mascotamodel',
            name='usuario',
        ),
        migrations.AddField(
            model_name='citamodel',
            name='citaEstado',
            field=models.IntegerField(choices=[(1, 'PENDIENTE'), (2, 'ECHO'), (2, 'CANCELADO')], db_column='cita_estado', default=1, verbose_name='Estado de la cita'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascotamodel',
            name='mascotaFoto',
            field=models.ImageField(db_column='mascota_foto', null=True, upload_to='mascota/', verbose_name='Foto de la mascota'),
        ),
        migrations.AddField(
            model_name='veterianriamodel',
            name='veterinariaCorreo',
            field=models.TextField(db_column='veterinaria_correo', default=None, verbose_name='veterinaria correo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veterianriamodel',
            name='veterinariaHorario',
            field=models.TextField(db_column='veterinaria_horario', default=None, verbose_name='Horario de la veterinaria'),
            preserve_default=False,
        ),
    ]
