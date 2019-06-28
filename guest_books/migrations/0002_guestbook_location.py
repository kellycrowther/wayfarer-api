# Generated by Django 2.2.1 on 2019-06-28 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waypoints', '0001_initial'),
        ('guest_books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbook',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_books', to='waypoints.Waypoint'),
        ),
    ]
