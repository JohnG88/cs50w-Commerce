from django.forms import ModelForm
from .models import *

class AuctionListForm(ModelForm):
    class Meta:
        model = AuctionListing
        exclude = ['user']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'entry']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude =['user', 'bid']

"""
class AuctionPriceUpdateForm(ModelForm):
    class Meta:
        model = AuctionListing
        exclude = ['title', 'description', 'photo', 'category']
"""
