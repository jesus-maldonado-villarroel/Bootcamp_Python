# Generated by Django 4.2 on 2024-05-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testdb', '0002_delete_adltest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adltest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(max_length=100)),
                ('valor1', models.IntegerField()),
            ],
        ),
    ]
