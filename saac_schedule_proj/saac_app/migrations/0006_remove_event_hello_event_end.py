# Generated by Django 5.1.2 on 2024-10-31 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saac_app', '0005_event_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='hello',
        ),
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 31, 5, 40, 45, 421434, tzinfo=datetime.timezone.utc)),
        ),
    ]