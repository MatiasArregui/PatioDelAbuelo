# Generated by Django 5.0.6 on 2024-05-24 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='id_factura',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.factura'),
        ),
    ]