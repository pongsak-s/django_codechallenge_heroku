from django.shortcuts import render

from .models import Student
from .models import School
from .serializers import StudentSerializer
from .serializers import SchoolSerializer

from rest_framework import viewsets
from rest_framework import permissions


class StudentViewSet(viewsets.ModelViewSet):
    """Represent viewset of student """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class StudentSchoolViewSet(viewsets.ModelViewSet):
    """Represent viewset of student (Relation) """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])


class SchoolViewSet(viewsets.ModelViewSet):
    """Represent viewset of school """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

