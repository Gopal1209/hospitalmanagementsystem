# Generated by Django 2.1.5 on 2019-09-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0038_auto_20190906_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='progress',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]