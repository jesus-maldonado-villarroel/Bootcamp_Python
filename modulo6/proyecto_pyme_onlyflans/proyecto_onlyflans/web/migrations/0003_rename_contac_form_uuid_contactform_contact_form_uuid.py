# Generated by Django 4.2 on 2024-05-01 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='contac_form_uuid',
            new_name='contact_form_uuid',
        ),
    ]
