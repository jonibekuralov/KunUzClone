# Generated by Django 4.2.10 on 2024-02-24 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_news_publish_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('mp4_file', models.FileField(upload_to='videos/')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 24, 19, 52, 34, 74220, tzinfo=datetime.timezone.utc)),
        ),
    ]
