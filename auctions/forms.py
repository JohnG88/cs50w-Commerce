from django.forms import ModelForm
from .models import *

class AuctionListForm(ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'price', 'photo', 'category']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'entry']
