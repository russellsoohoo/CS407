# Generated by Django 5.1.2 on 2024-10-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saac_app', '0002_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('subcommittee', models.CharField(choices=[('bo', 'BeOregon'), ('au', 'Athlete Unification'), ('dts', 'Duck The Stigma'), ('oh', 'OHeroes'), ('woo', 'Women Of Oregon'), ('s', 'SAAC'), ('dgp', 'Ducks Go Pro')], max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
