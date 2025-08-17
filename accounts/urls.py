from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('register/', UserViewSet.as_view({'post': 'register'}), name='register'),
    path('check-email/', UserViewSet.as_view({'get': 'check_email'}), name='check-email'),
    path('check-username/', UserViewSet.as_view({'get': 'check_username'}), name='check-username'),
    path('check-phone/', UserViewSet.as_view({'get': 'check_phone'}), name='check-phone'),
]