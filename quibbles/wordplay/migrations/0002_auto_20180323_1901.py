# Generated by Django 2.0.3 on 2018-03-23 18:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wordplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quibble',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 23, 18, 1, 10, 527841, tzinfo=utc)),
        ),
    ]
