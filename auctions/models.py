from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import ForeignKey


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    CATEGORY = (
        ("Accessories", "Accessories"),
        ("Books", "Books"),
        ("Electronics", "Electronics"),
        ("Food", "Food"),
        ("Garden", "Garden"),
        ("Home", "Home"),
        ("Music", "Music"),
        ("Office", "Office"),
        ("Safety", "Safety"),
        ("Video Games", "Video Games"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, choices=CATEGORY)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.ManyToManyField(AuctionListing)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    