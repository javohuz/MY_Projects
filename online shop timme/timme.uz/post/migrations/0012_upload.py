# Generated by Django 5.0 on 2023-12-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_rename_photo1k_post_photo5_remove_post_kumush_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(blank=True, max_length=200)),
                ('telnumber', models.CharField(blank=True, max_length=200)),
                ('linktitle', models.CharField(blank=True, max_length=200)),
                ('linkphoto', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
