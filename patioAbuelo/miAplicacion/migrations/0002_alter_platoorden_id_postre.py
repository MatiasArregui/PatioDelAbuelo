# Generated by Django 5.0.4 on 2024-06-08 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platoorden',
            name='id_postre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.postre'),
        ),
    ]