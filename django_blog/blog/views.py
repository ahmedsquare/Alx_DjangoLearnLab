from django.shortcuts import render

def home(request):
    return render(request, 'blog/base.html')  # Ensure 'blog/home.html' exists

def login_view(request):
    return render(request, 'blog/login.html')  # Ensure this template exists
    
def posts(request):
    return render(request, 'blog/posts.html')  # Ensure 'blog/posts.html' exists

def register_view(request):
    return render(request, 'blog/register.html')  # Ensure this template exists