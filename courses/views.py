from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsAdminOrReadOnly

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['level', 'instructor', 'is_active']
    search_fields = ['title', 'description', 'instructor']
    ordering_fields = ['price', 'created_at', 'title']
    ordering = ['-created_at']
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [IsAdminOrReadOnly()]
    
    def get_queryset(self):
        queryset = Course.objects.all()
        if hasattr(self.request, 'user') and self.request.user.is_authenticated and self.request.user.is_staff:
            return queryset
        return queryset.filter(is_active=True)