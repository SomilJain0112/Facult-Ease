# enrollment/serializers.py
from rest_framework import serializers
from .models import DegreeStatus, CourseStatus, Student, DegreeEnrollment, CourseEnrollment

class DegreeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeStatus
        fields = '__all__'

class CourseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStatus
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class DegreeEnrollmentSerializer(serializers.ModelSerializer):
    degree_code = serializers.CharField(source='degree.degree_code', read_only=True)
    class Meta:
        model = DegreeEnrollment
        fields = '__all__'

class CourseEnrollmentSerializer(serializers.ModelSerializer):
    student_code = serializers.CharField(source='degree_enrollment.student_code', read_only=True)
    class Meta:
        model = CourseEnrollment
        fields = '__all__'

class CourseEnrollmentSerializerWithDetail(CourseEnrollmentSerializer):
    degree_code = serializers.CharField(source='degree_enrollment.degree.degree_code', read_only=True)
    student_name = serializers.CharField(source='degree_enrollment.student.student_name', read_only=True)
    student_batch = serializers.CharField(source='degree_enrollment.batch', read_only=True)
    course_status_code = serializers.CharField(source='course_status.status_code', read_only=True)

