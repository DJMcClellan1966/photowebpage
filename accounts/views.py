from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error' : 'email address has already been used'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password2'])
                auth.login[request.user]
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error' : 'passwords must match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'photos/home.html')
