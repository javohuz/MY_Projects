# Generated by Django 5.0 on 2023-12-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20231203_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='NarxChegara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('dan', models.CharField(blank=True, max_length=200)),
                ('gacha', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
