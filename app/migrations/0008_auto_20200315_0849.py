# Generated by Django 3.0.3 on 2020-03-14 23:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20200314_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinout',
            name='check_in',
            field=models.TimeField(blank=True, null=True, verbose_name='出勤時刻'),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='check_out',
            field=models.TimeField(blank=True, null=True, verbose_name='退勤時刻'),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='date_worked',
            field=models.ForeignKey(default=datetime.date.today, on_delete=django.db.models.deletion.PROTECT, to='app.Date', verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='overtime_e',
            field=models.TimeField(blank=True, null=True, verbose_name='残業終了時刻'),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='overtime_s',
            field=models.TimeField(blank=True, null=True, verbose_name='残業開始時刻'),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='社員'),
        ),
        migrations.AlterField(
            model_name='date',
            name='masterdate',
            field=models.DateField(default=datetime.date.today, unique=True, verbose_name='日付'),
        ),
    ]
