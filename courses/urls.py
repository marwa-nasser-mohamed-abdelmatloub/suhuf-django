from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

# [AMS]:- Router for user API endpoints

router = DefaultRouter()
router.register(r'', CourseViewSet, basename='course')

app_name = 'courses'
urlpatterns = [
    path('', include(router.urls)),
]