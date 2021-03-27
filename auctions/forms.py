from django.forms import ModelForm
from .models import *

class AuctionListForm(ModelForm):
    class Meta:
        model = AuctionListing
        exclude = ['user']

class AuctionActiveUpdateForm(ModelForm):
    class Meta:
        model = AuctionListing
        exclude = ['user', 'title', 'description', 'price', 'photo', 'category',]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'entry']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude =['user', 'bid']
