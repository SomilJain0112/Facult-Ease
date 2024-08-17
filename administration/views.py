# administration/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Department, DegreeLevel, Semester, Degree
from .serializers import DepartmentSerializer, DegreeLevelSerializer, SemesterSerializer, DegreeSerializer
from courses.serializers import CourseDegreeSerializerWithDetail, CourseOccurrenceSerializerWithDetail, CourseSerializer
from faculties.serializers import ProfessorSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def degrees(self, request, pk=None):
        department = self.get_object()
        degrees = department.degrees.all()
        serializer = DegreeSerializer(degrees, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        department = self.get_object()
        courses = department.courses.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def professors(self, request, pk=None):
        department = self.get_object()
        professors = department.professors.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)

class DegreeLevelViewSet(viewsets.ModelViewSet):
    queryset = DegreeLevel.objects.all()
    serializer_class = DegreeLevelSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def degrees(self, request, pk=None):
        degree_level = self.get_object()
        degrees = degree_level.degrees.all()
        serializer = DegreeSerializer(degrees, many=True)
        return Response(serializer.data)

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def ongoing(self, request, pk=None):
        semester = self.get_object()
        course_occurrences = semester.course_occurrences.all()
        serializer = CourseOccurrenceSerializerWithDetail(course_occurrences, many=True)
        return Response(serializer.data)

class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        degree = self.get_object()
        course_degrees = degree.courses.all()
        serializer = CourseDegreeSerializerWithDetail(course_degrees, many=True)
        return Response(serializer.data)
