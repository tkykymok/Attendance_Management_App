# Generated by Django 3.0.3 on 2020-03-15 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200315_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinout',
            name='remark',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='備\u3000\u3000考'),
        ),
    ]
