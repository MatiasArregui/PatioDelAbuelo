# Generated by Django 5.0.4 on 2024-06-08 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0005_alter_bebidaorden_cantidad_alter_platoorden_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]
