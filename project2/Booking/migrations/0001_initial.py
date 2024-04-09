# Generated by Django 5.0.3 on 2024-04-09 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coach_payment', models.PositiveSmallIntegerField()),
                ('court_payment', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('confirm_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDatas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coach_refund', models.PositiveSmallIntegerField()),
                ('court_refund', models.PositiveSmallIntegerField()),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cancellation_time', models.DateTimeField(blank=True, null=True)),
                ('cancel_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(10.0)])),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review_from', models.CharField(choices=[('PLAYER', 'player'), ('COACH', 'coach')], max_length=10)),
            ],
        ),
    ]
