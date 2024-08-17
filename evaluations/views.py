# evaluations/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import EvaluationType, CourseOccurrenceEvaluation, StudentEvaluation, CourseGrades, SemesterGrades
from .serializers import EvaluationTypeSerializer, CourseOccurrenceEvaluationSerializer, StudentEvaluationSerializer, CourseGradesSerializer, SemesterGradesSerializer

class EvaluationTypeViewSet(viewsets.ModelViewSet):
    queryset = EvaluationType.objects.all()
    serializer_class = EvaluationTypeSerializer
    permission_classes = [IsAuthenticated]

class CourseOccurrenceEvaluationViewSet(viewsets.ModelViewSet):
    queryset = CourseOccurrenceEvaluation.objects.all()
    serializer_class = CourseOccurrenceEvaluationSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def evaluation_results(self, request, pk=None):
        evaluation = self.get_object()
        student_evaluations = evaluation.student_evaluations.all()
        serializer = StudentEvaluationSerializer(student_evaluations, many=True)
        return Response(serializer.data)

class StudentEvaluationViewSet(viewsets.ModelViewSet):
    queryset = StudentEvaluation.objects.all()
    serializer_class = StudentEvaluationSerializer
    permission_classes = [IsAuthenticated]

class CourseGradesViewSet(viewsets.ModelViewSet):
    queryset = CourseGrades.objects.all()
    serializer_class = CourseGradesSerializer
    permission_classes = [IsAuthenticated]

class SemesterGradesViewSet(viewsets.ModelViewSet):
    queryset = SemesterGrades.objects.all()
    serializer_class = SemesterGradesSerializer
    permission_classes = [IsAuthenticated]
