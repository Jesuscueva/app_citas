# Generated by Django 3.1.7 on 2021-04-06 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citas_veterinaria', '0004_auto_20210405_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciomodel',
            name='veterinaria',
            field=models.ForeignKey(db_column='veterinaria_id', on_delete=django.db.models.deletion.PROTECT, related_name='servicioVeterinaria', to='citas_veterinaria.veterianriamodel'),
        ),
        migrations.AlterField(
            model_name='veterinariomodel',
            name='veterinaria',
            field=models.ForeignKey(db_column='veterinaria_id', on_delete=django.db.models.deletion.PROTECT, related_name='veterinariosVeterinaria', to='citas_veterinaria.veterianriamodel'),
        ),
    ]