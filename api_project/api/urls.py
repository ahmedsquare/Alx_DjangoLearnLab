from .views import BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token 

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),  # Maps to the BookList view
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]