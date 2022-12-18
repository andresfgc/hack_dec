from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.events_list, name='events_list'),
    path('event/', views.event, name='event'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/', views.edit_event, name='edit_event'),
]
