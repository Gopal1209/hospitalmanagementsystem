# Generated by Django 2.1.5 on 2019-09-05 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0029_auto_20190905_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2019, 9, 5, 15, 27, 54, 974931)),
        ),
        migrations.AlterField(
            model_name='case',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 5, 15, 27, 54, 974931)),
        ),
    ]