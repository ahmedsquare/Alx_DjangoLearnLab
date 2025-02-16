from bookshelf.models import Book

# Retrieve a book instance
book = Book.objects.get(title="1984")

# delete a book
book.delete()

# Verify the delete
print(book)  # Output: empty

expected:
<>
