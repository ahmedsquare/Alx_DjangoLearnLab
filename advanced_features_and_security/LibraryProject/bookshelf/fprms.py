from django import forms
from .models import Book  # Assuming you have a Book model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title.isalnum():
            raise forms.ValidationError("Title should contain only letters and numbers.")
        return title
