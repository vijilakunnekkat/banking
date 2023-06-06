from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.context_processors import request


# Create your views here.
def home(request):
    return render(request,"home.html")

