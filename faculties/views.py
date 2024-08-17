# faculties/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Professor, ProfessorCourse
from .serializers import ProfessorSerializer, ProfessorCourseSerializer
from courses.serializers import CourseOccurrenceSerializerWithDetail

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def course_occurrences(self, request, pk=None):
        professor = self.get_object()
        course_occurrences = professor.course_occurrences.filter(is_active = True)
        serializer = CourseOccurrenceSerializerWithDetail(course_occurrences, many=True)
        return Response(serializer.data)

class ProfessorCourseViewSet(viewsets.ModelViewSet):
    queryset = ProfessorCourse.objects.all()
    serializer_class = ProfessorCourseSerializer
    permission_classes = [IsAuthenticated]
