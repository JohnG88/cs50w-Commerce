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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, choices=CATEGORY)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, null=True)
    new_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_bid_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    # if coming from an id or pk make sure to wrap up in str() to convert into a string
    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(AuctionListing, related_name='comments', null=True, on_delete=models.CASCADE)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return str(self.comment)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    #def __str__(self):
        #return self.user