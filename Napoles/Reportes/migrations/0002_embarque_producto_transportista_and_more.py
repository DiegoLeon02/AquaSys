# Generated by Django 5.0.6 on 2024-11-13 22:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embarque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='reporte',
            old_name='descripcion',
            new_name='acciones',
        ),
        migrations.RemoveField(
            model_name='reporte',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='reporte',
            name='tipo',
        ),
        migrations.AddField(
            model_name='reporte',
            name='fecha_generacion',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 1, 1, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporte',
            name='usuario',
            field=models.CharField(default=datetime.datetime(2024, 1, 1, 0, 0), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporte',
            name='embarque',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reportes', to='Reportes.embarque'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='embarque',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reportes.producto'),
        ),
        migrations.AddField(
            model_name='embarque',
            name='transportista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reportes.transportista'),
        ),
    ]
