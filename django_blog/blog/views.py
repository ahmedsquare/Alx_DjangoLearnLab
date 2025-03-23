from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

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

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'  # Ensure this template exists
    context_object_name = 'posts'
    ordering = ['-published_date']  # Show latest posts first

# Display a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Ensure this template exists

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'  # Ensure this template exists

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to the logged-in user
        return super().form_valid(form)

# Update a post (only by the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit

# Delete a post (only by the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')  # Redirect to post list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete