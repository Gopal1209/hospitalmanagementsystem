# Generated by Django 2.1.5 on 2019-09-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0046_current_cvisit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='temperature',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
