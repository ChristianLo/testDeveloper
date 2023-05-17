# Generated by Django 4.1.6 on 2023-05-17 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=150)),
                ('slots', models.IntegerField()),
                ('payment_terminal', models.BooleanField()),
                ('has_ebike', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='StationState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty_slots', models.IntegerField()),
                ('normal_bikes', models.IntegerField()),
                ('electric_bikes', models.IntegerField()),
                ('renting', models.BooleanField()),
                ('returning', models.BooleanField()),
                ('last_update', models.DateTimeField()),
                ('id_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tarea1.station')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tarea1.paymenttype')),
                ('id_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tarea1.station')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('id_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tarea1.station')),
            ],
        ),
    ]