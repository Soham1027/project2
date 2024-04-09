# Generated by Django 5.0.3 on 2024-04-09 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DataAvailability', '0001_initial'),
        ('SportingBuddiesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courtavailabilities',
            name='courts_ids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.courtdetails'),
        ),
        migrations.AddField(
            model_name='profileavailabilities',
            name='profiles_ids',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.profiles'),
        ),
    ]
