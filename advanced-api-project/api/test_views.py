from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from models import Book

class BookAPITest(TestCase):
    def setUp(self):
        """Set up test data and client authentication"""
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Log in the user (✅ Ensuring authenticated requests)
        self.client.login(username="testuser", password="testpass")

        # Sample Book object
        self.book = Book.objects.create(title="Django for Beginners", author="William S.", publication_year=2023)

    def test_list_books(self):
        """Test retrieving all books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book by ID"""
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_create_book_authenticated(self):
        """Ensure authenticated users can create books"""
        data = {"title": "New Book", "author": "Author X", "publication_year": 2024}
        response = self.client.post("/api/books/create/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books"""
        self.client.logout()  # ✅ Logout to simulate an unauthenticated user
        data = {"title": "Unauthorized Book", "author": "Anonymous", "publication_year": 2024}
        response = self.client.post("/api/books/create/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Expecting Forbidden

    def test_update_book_authenticated(self):
        """Ensure authenticated users can update books"""
        data = {"title": "Updated Title", "author": "William S.", "publication_year": 2023}
        response = self.client.put(f"/api/books/update/{self.book.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_update_book_unauthenticated(self):
        """Ensure unauthenticated users cannot update books"""
        self.client.logout()  # ✅ Logout before test
        data = {"title": "Hacked Title", "author": "Hacker", "publication_year": 2023}
        response = self.client.put(f"/api/books/update/{self.book.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Ensure authenticated users can delete books"""
        response = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_unauthenticated(self):
        """Ensure unauthenticated users cannot delete books"""
        self.client.logout()  # ✅ Logout before test
        response = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

