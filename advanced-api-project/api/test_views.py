from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from api.models import Book

class BookAPITest(TestCase):
    def setUp(self):
        """Set up test data and client authentication"""
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Log in the user
        self.client.login(username="testuser", password="testpass")  # ✅ Add this

        # Sample Book object
        self.book = Book.objects.create(title="Django for Beginners", author="William S.", publication_year=2023)

    def test_create_book_authenticated(self):
        """Ensure authenticated users can create books"""
        data = {"title": "New Book", "author": "Author X", "publication_year": 2024}
        response = self.client.post("/api/books/create/", data, format="json")

        self.assertEqual(response.status_code, 201)  # Expect 201 Created

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books"""
        self.client.logout()  # ✅ Logout before test
        data = {"title": "Unauthorized Book", "author": "Anonymous", "publication_year": 2024}
        response = self.client.post("/api/books/create/", data, format="json")

        self.assertEqual(response.status_code, 403)  # Expect 403 Forbidden

