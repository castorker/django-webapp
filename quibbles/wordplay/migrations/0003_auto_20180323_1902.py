# Generated by Django 2.0.3 on 2018-03-23 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wordplay', '0002_auto_20180323_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quibble',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
