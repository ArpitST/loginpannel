# Generated by Django 2.2.15 on 2020-10-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_post_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail_Image',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]