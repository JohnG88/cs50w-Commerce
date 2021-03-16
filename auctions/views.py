from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *


def index(request):
    entry = AuctionListing.objects.all()

    context = {'entry': entry}
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def createListing(request):
    form = AuctionListForm()
    if request.method == 'POST':
        form = AuctionListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "auctions/create_listingpage.html", context)

def listingPage(request, id):
    entry = AuctionListing.objects.get(id=id)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_item = comment_form.save(commit=False)
            
            comment_item.user = request.user
            comment_item.entry = entry
            comment_item.save()
            return HttpResponseRedirect(reverse('listingPage', args=[id]))
    
    context = {'entry': entry, 'comment_form': comment_form}
    return render(request, "auctions/listing_page.html", context)

def createBid(request):
    pass

def addComment(request):
    #add_comment = AuctionListing.addcomment_set.all()
    pass


def createWatchlist(request):
    entry_watch = Watchlist.objects.all()
    
    context = {'entry_watch': entry_watch}
    return render(request, "auctions/watchlist_page.html", context)



# from auctions.models import User, AuctionListing, Bid, Comment, Watchlist


# This line gives me all fields from User id=1(which in this case is the superuser)
# user1 = User.objects.get(id=1) 

# First use an object and assign it to model:
    # user_bid = Bid()
# Then add each field independently:
    # user_bid.user=user1.username(probably)
    # Then user_bid.save()

# Then to add the many to many field:
    # user_bid.bid.add(AuctionListing.objects.get(id=1)) (this line saves the instance)

# Then to add the other field:
    # user_bid.new_bid=1001
    # Then: user_bid.save()


# user_bid.bid.all() gives queryset [AuctionListing: Car]

# user_bid = Bid.objects.get(id=1)
#user_bid.bid.values('title')
    # QuerySet [{'title': 'Car'}]