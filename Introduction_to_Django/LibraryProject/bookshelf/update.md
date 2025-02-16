from bookshelf.models import Book

# Retrieve a book instance
book = Book.objects.get(title="1984")

# Update a field
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
print(book.title)  # Output: title

expected:
<1995>
