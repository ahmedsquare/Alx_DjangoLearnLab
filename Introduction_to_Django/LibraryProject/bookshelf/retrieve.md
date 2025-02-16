from bookshelf.models import Book


book = Book.objects.get(title="1984")
print(book)


expected:
<Book: 1984 by George Orwell, published on 1949-06-08>
