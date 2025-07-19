from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# [AMS]:- Router for user API endpoints
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('register/', UserViewSet.as_view({'post': 'register'}), name='register'),
]