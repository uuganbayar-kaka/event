from django.shortcuts import render,redirect,reverse
from . import forms, models
from .models import ProductImage, Product
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import modelformset_factory
from django.contrib import messages
from django.conf import settings

def home_view(request):
    return render(request, 'index.html')
    
#for showing login button for admin(by sumit)
def eventList(request):
    return render(request, 'event-listing.html')

def eventDetail(request):
    return render(request, 'event-detail.html')