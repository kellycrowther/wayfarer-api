# Generated by Django 2.2.1 on 2019-06-25 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waypoints', '0001_initial'),
        ('events', '0002_remove_event_waypoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='waypoints',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='waypoints.Waypoint'),
        ),
    ]
