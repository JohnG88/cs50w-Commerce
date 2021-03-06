# Generated by Django 3.1.6 on 2021-03-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlisting_bid_comment_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='new_bid',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='new_bid_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
