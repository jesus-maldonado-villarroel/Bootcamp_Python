# Generated by Django 4.2 on 2024-05-30 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('tipo_usuario', models.CharField(choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')], max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('m2_contruidos', models.FloatField()),
                ('m2_totales', models.FloatField()),
                ('cantidad_estacionamientos', models.IntegerField()),
                ('cantidad_habitaciones', models.IntegerField()),
                ('cantidad_baños', models.IntegerField()),
                ('direccion', models.CharField(max_length=250)),
                ('tipo_inmueble', models.CharField(choices=[('casa', 'Casa'), ('departamento', 'Departamento'), ('parcela', 'Parcela')], max_length=20)),
                ('precio_mensual', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
                ('id_comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmuebles.comuna')),
                ('id_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmuebles.region')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
