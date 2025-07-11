from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminOrReadOnly]