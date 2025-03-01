from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def is_member(user):
    if not hasattr(user, 'userprofile'):
        UserProfile.objects.create(user=user, role='Member')  # Default role if missing
    return user.is_authenticated and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
