from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NameForm, ContactForm



# Create your views here.
def index(request):
    return render(request,'posts/base.html')