# Generated by Django 4.0 on 2024-02-27 22:41

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
            name='TimeRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Days', models.IntegerField(choices=[(0, 'Saturday'), (1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday')])),
                ('workstart', models.TimeField()),
                ('workfinish', models.TimeField()),
                ('reststart', models.TimeField()),
                ('restfinish', models.TimeField()),
                ('duration', models.IntegerField(choices=[(15, '15 minute'), (30, '30 minute'), (45, '45 minute'), (60, '60 minute')])),
                ('number_timeslots', models.IntegerField(blank=True, null=True)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.barberprofile')),
            ],
            options={
                'unique_together': {('barber', 'Days')},
            },
        ),
        migrations.CreateModel(
            name='ExcludedDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.barberprofile')),
            ],
            options={
                'unique_together': {('date', 'barber')},
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(choices=[(datetime.date(2024, 2, 28), '2024-02-28 | (Wednesday)'), (datetime.date(2024, 2, 29), '2024-02-29 | (Thursday)'), (datetime.date(2024, 3, 1), '2024-03-01 | (Friday)'), (datetime.date(2024, 3, 2), '2024-03-02 | (Saturday)'), (datetime.date(2024, 3, 3), '2024-03-03 | (Sunday)'), (datetime.date(2024, 3, 4), '2024-03-04 | (Monday)'), (datetime.date(2024, 3, 5), '2024-03-05 | (Tuesday)'), (datetime.date(2024, 3, 6), '2024-03-06 | (Wednesday)'), (datetime.date(2024, 3, 7), '2024-03-07 | (Thursday)'), (datetime.date(2024, 3, 8), '2024-03-08 | (Friday)'), (datetime.date(2024, 3, 9), '2024-03-09 | (Saturday)'), (datetime.date(2024, 3, 10), '2024-03-10 | (Sunday)'), (datetime.date(2024, 3, 11), '2024-03-11 | (Monday)'), (datetime.date(2024, 3, 12), '2024-03-12 | (Tuesday)'), (datetime.date(2024, 3, 13), '2024-03-13 | (Wednesday)'), (datetime.date(2024, 3, 14), '2024-03-14 | (Thursday)'), (datetime.date(2024, 3, 15), '2024-03-15 | (Friday)'), (datetime.date(2024, 3, 16), '2024-03-16 | (Saturday)'), (datetime.date(2024, 3, 17), '2024-03-17 | (Sunday)'), (datetime.date(2024, 3, 18), '2024-03-18 | (Monday)'), (datetime.date(2024, 3, 19), '2024-03-19 | (Tuesday)')])),
                ('time', models.TimeField()),
                ('status', models.BooleanField(default=True)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.barberprofile')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customerprofile')),
            ],
            options={
                'unique_together': {('barber', 'date', 'time')},
            },
        ),
    ]
