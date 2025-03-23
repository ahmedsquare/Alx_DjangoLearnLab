from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Tag
from .forms import CommentForm
from .models import Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q

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

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comment_form'] = CommentForm()  # Initialize the comment form
        context['comments'] = post.comments.all()  # Fetch all comments related to the post
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('post_detail', pk=post.pk)  # Ensure this matches the URL name
        messages.error(request, 'There was an error with your comment submission.')
        return redirect('post_detail', pk=post.pk)
    # Create a new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        # Make sure the name is 'post-detail'
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})
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
    success_url = reverse_lazy('post-list')  # Redirect to post list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete



@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect('post_detail', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('post_detail', pk=comment.post.pk)

    post_pk = comment.post.pk
    comment.delete()
    messages.success(request, 'Comment deleted successfully!')
    return redirect('post_detail', pk=post_pk)

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        # Associate the comment with the current post and user
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        form.save()
        messages.success(self.request, 'Comment added successfully!')
        return redirect('post-detail', pk=post.pk)  # Redirect to the post detail view
    

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Comment updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the post detail view after updating the comment
        return self.object.post.get_absolute_url()
    

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'  # Create a confirmation template for deleting comments
    context_object_name = 'comment'

    def get_success_url(self):
        # After successful deletion, redirect to the post's detail page
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})
    


def search_posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})



def posts_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    return render(request, 'blog/tagged_posts.html', {'tag': tag, 'posts': posts})