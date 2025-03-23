from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'blog/base.html')  # Ensure 'blog/home.html' exists

def login_view(request):
    return render(request, 'blog/login.html')  # Ensure this template exists
    
def posts(request):
    return render(request, 'blog/posts.html')  # Ensure 'blog/posts.html' exists

def register_view(request):
    return render(request, 'blog/register.html')  # Ensure this template exists

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'blog/profile.html')
