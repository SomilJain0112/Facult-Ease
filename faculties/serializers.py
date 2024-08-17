from rest_framework import serializers
from .models import Professor, ProfessorCourse

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorCourseSerializer(serializers.ModelSerializer):
    professor_name = serializers.CharField(source='professor.display_name', read_only=True)
    course_code = serializers.CharField(source='course.course_code', read_only=True)

    class Meta:
        model = ProfessorCourse
        fields = '__all__'
