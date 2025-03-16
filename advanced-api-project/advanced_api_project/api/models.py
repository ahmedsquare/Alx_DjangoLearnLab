from django.db import models

"""Author ORM with Author Name and 
Function yo print the author name"""
class Author (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}\n"
"""Book ORM with Book Title and Publication_Year
and Author of the book"""    
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return f"{self.title} by {self.author}"
