# Generated by Django 2.1.7 on 2019-03-27 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartlink', '0012_auto_20190327_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
