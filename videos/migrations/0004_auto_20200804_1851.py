# Generated by Django 3.0.8 on 2020-08-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(null=True, upload_to=None),
        ),
    ]
