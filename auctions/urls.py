from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.createListing, name="createListing"),
    path("listingPage/<int:id>/", views.listingPage, name="listingPage"),
    path("add_Watchlist/<int:id>", views.add_Watchlist, name="add_Watchlist"),
    path("delete_Watchlist/<int:id>", views.delete_Watchlist, name="delete_Watchlist"),
    path("createWatchlist/", views.createWatchlist, name="createWatchlist"),
]
