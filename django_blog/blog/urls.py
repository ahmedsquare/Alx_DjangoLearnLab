from django.urls import path
from . import views
from .views import login_view
from .views import register_view  # Ensure you import your view

urlpatterns = [
    path('', views.home, name='home'),  # Define a default route for the blog
    path('posts/', views.posts, name='posts'),  # Add this line
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),

]
