from .models import Instructor , Course
from rest_framework import serializers

class CourseSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class InstructorSerlizer(serializers.ModelSerializer):
    courses = CourseSerlizer(many=True , read_only = True)
    class Meta:
        model = Instructor
        fields = '__all__'