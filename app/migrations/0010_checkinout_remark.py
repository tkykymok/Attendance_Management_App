# Generated by Django 3.0.3 on 2020-03-14 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200315_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkinout',
            name='remark',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='備考'),
        ),
    ]
