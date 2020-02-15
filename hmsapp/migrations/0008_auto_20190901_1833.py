# Generated by Django 2.1.5 on 2019-09-01 13:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0007_auto_20190901_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='visits',
            name='case_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='hmsapp.Case'),
        ),
        migrations.AlterField(
            model_name='case',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2019, 9, 1, 18, 33, 22, 258352)),
        ),
        migrations.AlterField(
            model_name='case',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 1, 18, 33, 22, 258352)),
        ),
    ]