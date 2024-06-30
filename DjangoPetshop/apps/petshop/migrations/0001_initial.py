# Generated by Django 5.0.6 on 2024-06-26 23:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('sku', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='imagenes_categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('gmail', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('sku', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField(max_length=10)),
                ('stock', models.IntegerField(max_length=10)),
                ('img', models.ImageField(upload_to='imagenes_producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petshop.categoria')),
            ],
        ),
    ]
