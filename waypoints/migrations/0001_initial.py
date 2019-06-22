# Generated by Django 2.2.1 on 2019-06-22 04:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waypoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('subtitle', models.CharField(blank=True, default='', max_length=150)),
                ('description', models.TextField()),
                ('rating', models.IntegerField()),
                ('favorite', models.IntegerField()),
                ('waypointType', models.IntegerField(choices=[(0, ''), (1, 'Urban'), (2, 'Country'), (3, 'Rural'), (4, 'Mountainous'), (5, 'Desert'), (6, 'Restaurant'), (7, 'Park'), (8, 'Coffee Shop')], default=0)),
                ('photo', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('address', models.TextField()),
                ('state', models.TextField()),
                ('zipCode', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
