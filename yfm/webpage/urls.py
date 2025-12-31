from django.urls import path
from .views import HomeListView
from . import views
from django.shortcuts import render

urlpatterns = [ #important - list, not set {} !
    path('', view=HomeListView.as_view(), name='base'),
    #path('booking/', views.booking, name='booking'), #booking form handling rezerwacja-django


    # Calendar and Booking URLs
    path("day/<str:day>/", views.times_view, name="times"), #Hours in new page
    #path("day/<str:day>/", view=HomeListView.as_view(), name="base"), #WIP #Hours in base.html
    path("book/<int:slot_id>/", views.book_view, name="book"),
    path("success/", lambda r: render(r, "success.html"), name="success"), #TODO
    path("contact/", views.contact_view, name="contact"),
]