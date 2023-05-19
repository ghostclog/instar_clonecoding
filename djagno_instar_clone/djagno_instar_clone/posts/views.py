from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NameForm, ContactForm



# Create your views here.
def index(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            return HttpResponseRedirect('/myform/thanks')
    else:
        form = NameForm()
    return render(request,'myform/name.html',{"form":form})

