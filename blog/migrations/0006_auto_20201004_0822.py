# Generated by Django 2.2.15 on 2020-10-04 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201003_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagging',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='tagging',
            name='taggings',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Tagging',
        ),
    ]