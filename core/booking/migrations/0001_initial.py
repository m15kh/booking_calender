# Generated by Django 4.0 on 2023-10-27 17:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TimeRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Days', models.IntegerField(choices=[(0, 'Saturday'), (1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday')], unique=True)),
                ('startwork', models.TimeField()),
                ('finishwork', models.TimeField()),
                ('startrest', models.TimeField()),
                ('finishrest', models.TimeField()),
                ('duration', models.IntegerField(choices=[(15, '15 minute'), (30, '30 minute'), (45, '45 minute'), (60, '60 minute')])),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(choices=[(datetime.date(2023, 10, 20), '2023-10-20 (Friday)'), (datetime.date(2023, 10, 21), '2023-10-21 (Saturday)'), (datetime.date(2023, 10, 22), '2023-10-22 (Sunday)'), (datetime.date(2023, 10, 23), '2023-10-23 (Monday)'), (datetime.date(2023, 10, 24), '2023-10-24 (Tuesday)'), (datetime.date(2023, 10, 25), '2023-10-25 (Wednesday)'), (datetime.date(2023, 10, 26), '2023-10-26 (Thursday)'), (datetime.date(2023, 10, 27), '2023-10-27 (Friday)'), (datetime.date(2023, 10, 28), '2023-10-28 (Saturday)'), (datetime.date(2023, 10, 29), '2023-10-29 (Sunday)'), (datetime.date(2023, 10, 30), '2023-10-30 (Monday)'), (datetime.date(2023, 10, 31), '2023-10-31 (Tuesday)'), (datetime.date(2023, 11, 1), '2023-11-01 (Wednesday)'), (datetime.date(2023, 11, 2), '2023-11-02 (Thursday)'), (datetime.date(2023, 11, 3), '2023-11-03 (Friday)'), (datetime.date(2023, 11, 4), '2023-11-04 (Saturday)'), (datetime.date(2023, 11, 5), '2023-11-05 (Sunday)'), (datetime.date(2023, 11, 6), '2023-11-06 (Monday)'), (datetime.date(2023, 11, 7), '2023-11-07 (Tuesday)'), (datetime.date(2023, 11, 8), '2023-11-08 (Wednesday)'), (datetime.date(2023, 11, 9), '2023-11-09 (Thursday)')])),
                ('timeslot', models.TimeField()),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.barber')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
            options={
                'unique_together': {('barber', 'date', 'timeslot')},
            },
        ),
    ]
