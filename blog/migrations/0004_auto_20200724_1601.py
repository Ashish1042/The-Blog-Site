# Generated by Django 3.0.3 on 2020-07-24 10:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200724_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 24, 10, 31, 45, 445483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 24, 10, 31, 45, 445483, tzinfo=utc)),
        ),
    ]
