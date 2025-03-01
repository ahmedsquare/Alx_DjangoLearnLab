from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book  # Ensure Library is imported
from .models import Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect to books list after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# User Registration View
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the new user automatically
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



# def is_admin(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_dashboard.html')


# def is_librarian(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_dashboard.html')


# def is_member(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_dashboard.html')
