from bookshelf.models import Book


book = Book.objects.create(title="1984", author="George Orwell", published_date="1949-06-08")
print(book)

book = Book.objects.get(title="1984")
print(book)

expected:
<Book: 1984 by George Orwell, published on 1949-06-08>
