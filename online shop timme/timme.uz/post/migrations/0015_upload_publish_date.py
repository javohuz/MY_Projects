# Generated by Django 5.0 on 2023-12-28 15:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_alter_narxchegara_dan_alter_narxchegara_gacha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
