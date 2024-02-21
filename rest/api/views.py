from django.shortcuts import render
from .seralizers import InstructorSerlizer , CourseSerlizer
from .models import Course , Instructor
from rest_framework import generics

# Create your views here.
class InsulatorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerlizer
    queryset = Instructor.objects.all()
    
class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerlizer
    queryset = Course.objects.all()
    
