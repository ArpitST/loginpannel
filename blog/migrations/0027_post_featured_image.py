# Generated by Django 2.2.15 on 2020-10-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_Image',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
