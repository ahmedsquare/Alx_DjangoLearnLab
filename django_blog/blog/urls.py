from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.posts, name='posts'),
    path('postslist/', PostListView.as_view(), name='post-list'),  # List all posts
    path('postslist/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('postslist/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a post
    path('postslist/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('postslist/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
]