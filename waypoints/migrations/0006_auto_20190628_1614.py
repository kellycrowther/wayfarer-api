# Generated by Django 2.2.1 on 2019-06-28 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waypoints', '0005_auto_20190628_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinate',
            name='waypoint',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coordinate', to='waypoints.Waypoint'),
        ),
    ]
