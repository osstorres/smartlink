# Generated by Django 2.1.7 on 2019-05-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0027_auto_20190508_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='relacion_tec',
            field=models.CharField(choices=[('Alumno Profesional/Preparatoria', 'Alumno Profesional/Preparatoria'), ('Exatec', 'Exatec'), ('Alumno Maestria Tec', 'Alumno Maestria Tec'), ('Incubado Tec', 'Incubado Tec'), ('Consejero Tec', 'Consejero Tec'), ('Empleado Tec', 'Empleado Tec'), ('Papa/Mama Tec', 'Papa/Mama Tec'), ('Ninguna', 'Ninguna')], default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='tipo_invitacion',
            field=models.CharField(choices=[('Alumno Profesional/Preparatoria', 'Alumno Profesional/Preparatoria'), ('Exatec', 'Exatec'), ('Alumno Maestria Tec', 'Alumno Maestria Tec'), ('Incubado Tec', 'Incubado Tec'), ('Consejero Tec', 'Consejero Tec'), ('Empleado Tec', 'Empleado Tec'), ('Papa/Mama Tec', 'Papa/Mama Tec'), ('General', 'General')], default=None, max_length=200),
        ),
    ]
