# Generated by Django 4.2.7 on 2023-11-14 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_alter_reserva_idapartamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='idApartamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.zonasc'),
        ),
    ]