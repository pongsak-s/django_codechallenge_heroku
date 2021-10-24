from rest_framework import serializers
from .models import Student
from .models import School

class StudentSerializer(serializers.ModelSerializer):
    """Represent serializer of student """

    class Meta:
        model = Student 
        fields = ['pk', 'firstname', 'lastname', 'studentid', 'created', 'school']


class SchoolSerializer(serializers.ModelSerializer):
    """Represent serializer of school """

    class Meta:
        model = School 
        fields = ['pk', 'name', 'max_students', 'created']