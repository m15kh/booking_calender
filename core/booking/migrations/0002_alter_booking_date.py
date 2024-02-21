# Generated by Django 4.0 on 2024-02-08 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(choices=[(datetime.date(2024, 2, 8), '2024-02-08 | (Thursday)'), (datetime.date(2024, 2, 9), '2024-02-09 | (Friday)'), (datetime.date(2024, 2, 10), '2024-02-10 | (Saturday)'), (datetime.date(2024, 2, 11), '2024-02-11 | (Sunday)'), (datetime.date(2024, 2, 12), '2024-02-12 | (Monday)'), (datetime.date(2024, 2, 13), '2024-02-13 | (Tuesday)'), (datetime.date(2024, 2, 14), '2024-02-14 | (Wednesday)'), (datetime.date(2024, 2, 15), '2024-02-15 | (Thursday)'), (datetime.date(2024, 2, 16), '2024-02-16 | (Friday)'), (datetime.date(2024, 2, 17), '2024-02-17 | (Saturday)'), (datetime.date(2024, 2, 18), '2024-02-18 | (Sunday)'), (datetime.date(2024, 2, 19), '2024-02-19 | (Monday)'), (datetime.date(2024, 2, 20), '2024-02-20 | (Tuesday)'), (datetime.date(2024, 2, 21), '2024-02-21 | (Wednesday)'), (datetime.date(2024, 2, 22), '2024-02-22 | (Thursday)'), (datetime.date(2024, 2, 23), '2024-02-23 | (Friday)'), (datetime.date(2024, 2, 24), '2024-02-24 | (Saturday)'), (datetime.date(2024, 2, 25), '2024-02-25 | (Sunday)'), (datetime.date(2024, 2, 26), '2024-02-26 | (Monday)'), (datetime.date(2024, 2, 27), '2024-02-27 | (Tuesday)'), (datetime.date(2024, 2, 28), '2024-02-28 | (Wednesday)')]),
        ),
    ]