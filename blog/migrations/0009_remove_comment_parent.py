# Generated by Django 2.2.15 on 2020-10-05 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
