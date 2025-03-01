from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def admin_check(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


@user_passes_test(admin_check)
def admin_view(request):
    return HttpResponse("Welcome to the Admin View")  # No rendering, plain text response