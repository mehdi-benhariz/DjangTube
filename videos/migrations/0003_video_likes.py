# Generated by Django 3.0.8 on 2020-08-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20200803_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
