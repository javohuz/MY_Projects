# Generated by Django 3.1.14 on 2023-12-02 18:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20231202_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='batafsil',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='narxi',
            new_name='narxi1',
        ),
        migrations.AddField(
            model_name='post',
            name='mahsulotTavsifi',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sharhsoni',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='stars',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]