# Generated by Django 4.2.15 on 2024-08-28 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
