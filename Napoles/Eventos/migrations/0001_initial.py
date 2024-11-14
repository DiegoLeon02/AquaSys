# Generated by Django 5.0.6 on 2024-11-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=100)),
                ('responsable', models.CharField(max_length=100)),
            ],
        ),
    ]
