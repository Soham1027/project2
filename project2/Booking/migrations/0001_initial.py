# Generated by Django 4.2 on 2024-04-19 08:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SportingBuddiesApp', '0001_initial'),
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
                ('coach_data_ids', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.coaches')),
                ('ground_provider_ids', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.groundproviders')),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='SportingBuddiesApp.players')),
                ('player_2', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='SportingBuddiesApp.players')),
                ('player_3', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_3', to='SportingBuddiesApp.players')),
                ('player_data_ids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_id', to='SportingBuddiesApp.players')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.profiles')),
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
                ('coach_data_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.coaches')),
                ('players_data_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SportingBuddiesApp.players')),
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
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.bookings')),
            ],
        ),
    ]
