# Generated by Django 2.1.5 on 2019-09-02 14:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0018_auto_20190902_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='visits',
            name='case_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='hmsapp.Case'),
        ),
        migrations.AlterField(
            model_name='case',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2019, 9, 2, 20, 13, 34, 271500)),
        ),
        migrations.AlterField(
            model_name='case',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 2, 20, 13, 34, 271500)),
        ),
    ]