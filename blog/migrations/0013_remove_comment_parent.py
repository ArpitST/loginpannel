# Generated by Django 2.2.15 on 2020-10-07 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
