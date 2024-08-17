# courses/serializers.py
from rest_framework import serializers
from .models import Course, CourseDegree, CourseDependency, CourseOccurrence

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDegree
        fields = '__all__'

class CourseDegreeSerializerWithDetail(CourseDegreeSerializer):
    course_code = serializers.CharField(source='course.course_code', read_only=True)
    degree_code = serializers.CharField(source='degree.degree_code', read_only=True)
    course_name = serializers.CharField(source='course.course_name', read_only=True)

class CourseDependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDependency
        fields = '__all__'

class CourseOccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOccurrence
        fields = '__all__'

class CourseOccurrenceSerializerWithDetail(CourseOccurrenceSerializer):
    professor_name = serializers.CharField(source='professor.display_name', read_only=True)
    course_code = serializers.CharField(source='course.course_code', read_only=True)
    assistant_professor_name = serializers.SerializerMethodField()

    def get_assistant_professor_name(self, obj):
        return obj.assistant_professor.display_name if obj.assistant_professor else None