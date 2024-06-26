# Generated by Django 5.0.4 on 2024-06-08 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0003_alter_platoorden_id_postre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platoorden',
            name='id_bebida',
        ),
        migrations.RemoveField(
            model_name='platoorden',
            name='id_postre',
        ),
        migrations.CreateModel(
            name='BebidaOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_bebida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.bebida')),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.orden')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='id_bebida',
            field=models.ManyToManyField(through='miAplicacion.BebidaOrden', to='miAplicacion.bebida'),
        ),
        migrations.CreateModel(
            name='PostreOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.orden')),
                ('id_postre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.postre')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='id_postre',
            field=models.ManyToManyField(through='miAplicacion.PostreOrden', to='miAplicacion.postre'),
        ),
    ]
