from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def is_librarian(user):
    if not hasattr(user, 'userprofile'):
        UserProfile.objects.create(user=user, role='Member')  # Default role if missing
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
