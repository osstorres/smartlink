# Generated by Django 2.1.7 on 2019-03-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0013_auto_20190327_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
