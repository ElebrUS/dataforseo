# Generated by Django 3.1.7 on 2021-03-10 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210310_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='engine',
            field=models.CharField(max_length=256, verbose_name='Search Engine'),
        ),
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 11, 19, 30, 261307), verbose_name='Date Add'),
        ),
    ]
