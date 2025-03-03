from django.contrib import admin
from .models import Book
from .models import CustomUser  # Import your CustomUser model
from django.contrib.auth.admin import UserAdmin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author')
    list_filter = ('publication_date',)






class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('id',)

# Register CustomUser with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
