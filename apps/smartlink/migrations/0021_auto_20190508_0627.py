# Generated by Django 2.1.7 on 2019-05-08 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0020_auto_20190508_0610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choices',
            old_name='tipo_invitacion',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='eventos',
            old_name='tipo_invitacion',
            new_name='tipo',
        ),
    ]
