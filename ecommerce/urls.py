from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home_view, name=''),
    path('event-list', views.eventList, name='event-list'),
    path('event-detail', views.eventDetail, name='event-detail'),
]
