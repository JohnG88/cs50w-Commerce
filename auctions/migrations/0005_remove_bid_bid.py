# Generated by Django 3.1.6 on 2021-03-19 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_comment_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bid',
        ),
    ]
