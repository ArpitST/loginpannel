# Generated by Django 2.2.15 on 2020-10-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20201009_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_Image',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]