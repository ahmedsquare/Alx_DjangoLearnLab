from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def is_admin(user):
    if not hasattr(user, 'userprofile'):
        UserProfile.objects.create(user=user, role='Member')  # Default role if missing
    return user.is_authenticated and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
