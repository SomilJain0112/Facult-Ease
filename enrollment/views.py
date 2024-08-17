# enrollment/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DegreeStatus, CourseStatus, Student, DegreeEnrollment, CourseEnrollment
from .serializers import DegreeStatusSerializer, CourseStatusSerializer, StudentSerializer, DegreeEnrollmentSerializer, CourseEnrollmentSerializer
from evaluations.serializers import StudentEvaluationSerializer
from collections import defaultdict

class DegreeStatusViewSet(viewsets.ModelViewSet):
    queryset = DegreeStatus.objects.all()
    serializer_class = DegreeStatusSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def enrollments(self, request, pk=None):
        degree_status = self.get_object()
        enrollments = degree_status.degree_enrollments.all()
        serializer = DegreeEnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

class CourseStatusViewSet(viewsets.ModelViewSet):
    queryset = CourseStatus.objects.all()
    serializer_class = CourseStatusSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def enrollments(self, request, pk=None):
        course_status = self.get_object()
        enrollments = course_status.course_enrollments.all()
        serializer = CourseEnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def degrees(self, request, pk=None):
        student = self.get_object()
        degrees = student.degree_enrollments.all()
        serializer = DegreeEnrollmentSerializer(degrees, many=True)
        return Response(serializer.data)

class DegreeEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = DegreeEnrollment.objects.all()
    serializer_class = DegreeEnrollmentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        degree_enrollment = self.get_object()
        courses = degree_enrollment.course_enrollments.all()
        serializer = CourseEnrollmentSerializer(courses, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def semester_grades(self, request, pk=None):
        degree_enrollment = self.get_object()
        
        # Retrieve all semester grades and course enrollments for the degree enrollment
        semester_grades = degree_enrollment.semester_grades.all()
        course_enrollments = degree_enrollment.course_enrollments.all()
        
        # Organize the data into a nested structure
        data = defaultdict(lambda: {"courses": {}, "semester_grade": {}})
        
        for semester_grade in semester_grades:
            semester_number = semester_grade.semester_number
            data[semester_number]["semester_grade"] = semester_grade.sgpa
        
        for course_enrollment in course_enrollments:
            course_grade = course_enrollment.grades
            
            if course_grade:
                semester_number = course_enrollment.semester_number
                course_id = course_enrollment.course_occurrence.course.id
                course_code = course_enrollment.course_occurrence.course.code
                data[semester_number]["courses"][course_id] = {
                    "course":course_code,
                    "greade":course_grade.grade
                }
        
        return Response(data)

class CourseEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def evaluations(self, request, pk=None):
        course_enrollment = self.get_object()
        evaluations = course_enrollment.student_evaluations.all()
        serializer = StudentEvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)
