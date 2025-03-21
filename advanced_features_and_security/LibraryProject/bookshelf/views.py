from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from .forms import ExampleForm

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        Book.objects.create(title=title, author=author, published_date=published_date)
        return render(request, 'books/book_created.html')
    return render(request, 'books/book_create.html')

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return render(request, 'books/book_edited.html')
    return render(request, 'books/book_edit.html', {'book': book})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'books/book_deleted.html')



def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to the database, send an email, etc.)
            return render(request, 'bookshelf/form_success.html', {'form': form})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

