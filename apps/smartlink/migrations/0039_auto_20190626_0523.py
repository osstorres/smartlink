# Generated by Django 2.1.7 on 2019-06-26 05:23

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0038_auto_20190626_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='tipo_invitacion',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Alumno Profesional/Preparatoria', 'Alumno Profesional/Preparatoria'), ('Exatec', 'Exatec'), ('Alumno Maestria Tec', 'Alumno Maestria Tec'), ('Incubado Tec', 'Incubado Tec'), ('Consejero Tec', 'Consejero Tec'), ('Empleado Tec', 'Empleado Tec'), ('Papá/Mamá Tec', 'Papá/Mamá Tec'), ('General', 'General')], default=None, max_length=120),
        ),
    ]