# Generated by Django 5.1.2 on 2024-10-31 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saac_app', '0008_event_location_alter_event_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
    ]
