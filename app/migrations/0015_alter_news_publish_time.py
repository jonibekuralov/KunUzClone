# Generated by Django 4.2.10 on 2024-02-27 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_news_publish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 18, 19, 24, 592982, tzinfo=datetime.timezone.utc)),
        ),
    ]
