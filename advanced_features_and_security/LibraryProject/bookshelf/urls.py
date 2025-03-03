from django.urls import path
from .views import example_form_view
from .views import book_list

urlpatterns = [
    path('example-form/', example_form_view, name='example_form'),
    path('books/', book_list, name='book-list'),

]
