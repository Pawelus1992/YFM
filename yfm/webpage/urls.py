from django.urls import path
from .views import HomeListView
from . import views
from django.shortcuts import render

urlpatterns = [ #important - list, not set {} !
    path('', view=HomeListView.as_view(), name='base'),
    # Calendar and Booking URLs
    path("day/<str:day>/", views.times_view, name="times"), #TODO Hours in new page
    path("book/<int:slot_id>/", views.book_view, name="book"),
    path("success/", lambda r: render(r, "success.html"), name="success"),
    path("contact/", views.contact_view, name="contact"),
]