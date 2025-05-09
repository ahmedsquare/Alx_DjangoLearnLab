from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book  # Ensure Library is imported
from .models import Library
from .models import Author
from .forms import BookForm  # Import the form

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required

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
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the new user automatically
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@login_required
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@login_required
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, "relationship_app/member_view.html")

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the book with user input
            return redirect('list_books')  # Redirect to book list after adding
    else:
        form = BookForm()

    return render(request, 'relationship_app/add_book.html', {'form': form})


@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request,book_id):
    book = get_object_or_404(Book , id = book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance= book)
        if form.is_valid():
            form.save()  # Save the book with user input
            return redirect('list_books')  # Redirect to book list after adding
    else:
        form = BookForm(instance=book)

    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book':book})



@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request,book_id):
    book = get_object_or_404(Book , id = book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')


    return render(request, 'relationship_app/delete_book.html', {'book':book})