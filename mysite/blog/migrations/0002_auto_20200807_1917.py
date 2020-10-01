# Generated by Django 3.0.3 on 2020-08-07 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 13, 47, 47, 775227, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 13, 47, 47, 773233, tzinfo=utc)),
        ),
    ]