# Generated by Django 5.0.6 on 2024-05-24 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('Total', models.IntegerField()),
                ('Id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('id_factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.factura')),
                ('id_mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.mesa')),
            ],
        ),
        migrations.CreateModel(
            name='PlatoOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.orden')),
                ('id_plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.plato')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='id_plato',
            field=models.ManyToManyField(through='miAplicacion.PlatoOrden', to='miAplicacion.plato'),
        ),
    ]