# Generated by Django 4.2.7 on 2023-11-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_pqrsd'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZonasC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=250)),
                ('Horario', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=250)),
            ],
        ),
    ]