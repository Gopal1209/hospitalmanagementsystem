# Generated by Django 2.1.5 on 2019-09-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0042_auto_20190906_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmedic', models.IntegerField()),
                ('clab', models.IntegerField()),
            ],
        ),
    ]
