# Generated by Django 5.0.6 on 2024-11-18 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0002_loginactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginactivity',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfiles', to='Administrador.perfil'),
        ),
    ]
