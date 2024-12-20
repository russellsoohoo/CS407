# Generated by Django 5.1.2 on 2024-12-04 18:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saac_app', '0014_alter_customuser_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registered_users',
            field=models.ManyToManyField(blank=True, related_name='registered_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sport',
            field=models.CharField(choices=[('W Acrobatics & Tumbling', 'W Acrobatics & Tumbling'), ('W Basketball', 'W Basketball'), ('W Beach Volleyball', 'W Beach Volleyball'), ('W Cross Country', 'W Cross Country'), ('W Golf', 'W Golf'), ('W Lacrosse', 'W Lacrosse'), ('W Soccer', 'W Soccer'), ('W Softball', 'W Softball'), ('W Tennis', 'W Tennis'), ('W Track & Field', 'W Track & Field'), ('W Volleyball', 'W Volleyball'), ('M Baseball', 'M Baseball'), ('M Basketball', 'M Basketball'), ('M Cross Country', 'M Cross Country'), ('M Football', 'M Football'), ('M Golf', 'M Golf'), ('M Tennis', 'M Tennis'), ('M Track & Field', 'M Track & Field')], max_length=25),
        ),
    ]
