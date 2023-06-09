from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignUp

def main(request):
    if request.method == 'GET':
        return render(request,'users/main.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['username']
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('posts:index'))
        else:
            return render(request,'users/main.html')    #4분6초 서버 열었을때 탬플릿 연결되는지 확인
        
def signup(request):
    if request.method == 'GET':
        form = SignUp()
        return render(request, 'user/signup.html',{'form': form })
    
    elif request.method == 'POST':
        form = SignUp(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('posts:index'))

        return render(request,'users/main.html')
            
