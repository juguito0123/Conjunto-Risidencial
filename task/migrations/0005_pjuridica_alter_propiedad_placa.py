# Generated by Django 4.2.7 on 2023-11-14 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_propiedad'),
    ]

    operations = [
        migrations.CreateModel(
            name='PJuridica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=250)),
                ('contacto', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='placa',
            field=models.CharField(max_length=100),
        ),
    ]
