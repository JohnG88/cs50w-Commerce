# Generated by Django 3.1.6 on 2021-03-20 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bid_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
