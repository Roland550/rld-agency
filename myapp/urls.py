from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name=" index"),
    path('destination', views.destination, name=" destination"),
    path('ticket', views.ticket, name="ticket"),
    path('contact', views.contact, name="contact"),
] 