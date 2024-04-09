# Generated by Django 5.0.3 on 2024-04-09 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTimes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourtAvailabilities',
            fields=[
                ('datatimes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DataAvailability.datatimes')),
            ],
            bases=('DataAvailability.datatimes',),
        ),
        migrations.CreateModel(
            name='ProfileAvailabilities',
            fields=[
                ('datatimes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DataAvailability.datatimes')),
            ],
            bases=('DataAvailability.datatimes',),
        ),
    ]
