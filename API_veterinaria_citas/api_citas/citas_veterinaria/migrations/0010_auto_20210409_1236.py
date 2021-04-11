# Generated by Django 3.1.7 on 2021-04-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas_veterinaria', '0009_auto_20210409_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinariomodel',
            name='veterinarioApellido',
            field=models.CharField(db_column='veterinario_apellido', max_length=45, verbose_name='Apellido de la veterinario'),
        ),
        migrations.AlterField(
            model_name='veterinariomodel',
            name='veterinarioNombre',
            field=models.CharField(db_column='veterinario_nombre', max_length=45, verbose_name='Nombre de la veterinario'),
        ),
    ]