from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request=request,user=user)
            return redirect('chatapp:index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect("users:login")

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("users:login")
    
    return render(request, "users/signup.html")