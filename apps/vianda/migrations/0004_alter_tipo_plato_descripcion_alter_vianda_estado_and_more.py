# Generated by Django 4.1.3 on 2022-11-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vianda', '0003_alter_vianda_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_plato',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vianda',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'pendiente'), ('Confirmado', 'confirmado'), ('Cancelado', 'cancelado')], default='Pendiente', max_length=200),
        ),
        migrations.AlterField(
            model_name='vianda',
            name='fecha_inicio_vianda',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vianda',
            name='frecuencia',
            field=models.CharField(choices=[('Semanal', 'semanal'), ('Quincenal', 'quincenal')], max_length=200),
        ),
        migrations.AlterField(
            model_name='vianda',
            name='tipo_menu',
            field=models.CharField(choices=[('Normal', 'normal'), ('Diabetico', 'diabetico'), ('Vegetariano', 'vegetariano')], max_length=200),
        ),
        migrations.RemoveField(
            model_name='vianda',
            name='tipo_platos',
        ),
        migrations.AddField(
            model_name='vianda',
            name='tipo_platos',
            field=models.ManyToManyField(to='vianda.tipo_plato'),
        ),
    ]
