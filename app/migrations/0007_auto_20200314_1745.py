# Generated by Django 3.0.3 on 2020-03-14 08:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200314_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinout',
            name='date_worked',
            field=models.ForeignKey(default=datetime.date.today, on_delete=django.db.models.deletion.PROTECT, to='app.Date'),
        ),
    ]
