# Generated by Django 2.1.5 on 2019-09-06 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0041_auto_20190906_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medic',
            old_name='visit_id',
            new_name='visit',
        ),
    ]
