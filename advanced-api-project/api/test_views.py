from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from myapp.models import Book

class BookAPITestCase(TestCase):
    """Test suite for the Book API endpoints"""

    def setUp(self):
        """Set up test data and client"""
        self.client = APIClient()
        
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        # Create sample books
        self.book1 = Book.objects.create(title="Django for Beginners", author="William S. Vincent", publication_year=2021)
        self.book2 = Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2019)

        self.valid_data = {"title": "REST API with Django", "author": "Ahmed Ahmed", "publication_year": 2024}
        self.invalid_data = {"title": "", "author": "No Name", "publication_year": "invalid"}

    def test_list_books(self):
        """Test retrieving all books"""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return two books

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Django for Beginners")

    def test_create_book(self):
        """Test creating a book"""
        response = self.client.post('/api/books/create/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_invalid(self):
        """Test creating a book with invalid data"""
        response = self.client.post('/api/books/create/', self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book(self):
        """Test updating a book"""
        response = self.client.put(f'/api/books/update/{self.book1.id}/', {"title": "Updated Django Book"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """Test filtering books by author"""
        response = self.client.get('/api/books/?author=Eric Matthes')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "Eric Matthes")

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get('/api/books/?search=Django')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Django" in book['title'] for book in response.data))

    def test_order_books(self):
        """Test ordering books by publication_year"""
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2019)  # Oldest first

    def test_unauthorized_access(self):
        """Test unauthorized access restriction"""
        self.client.logout()
        response = self.client.post('/api/books/create/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
