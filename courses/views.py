# courses/views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, CourseDegree, CourseDependency, CourseOccurrence
from .serializers import CourseSerializer, CourseDegreeSerializer, CourseDependencySerializer, CourseOccurrenceSerializer, CourseOccurrenceSerializerWithDetail, CourseDegreeSerializerWithDetail
from enrollment.serializers import CourseEnrollmentSerializerWithDetail
from evaluations.serializers import CourseOccurrenceEvaluationSerializer, StudentEvaluationSerializer
from faculties.serializers import ProfessorSerializer
from collections import defaultdict

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def occurrences(self, request, pk=None):
        course = self.get_object()
        semester_id = request.query_params.get('semester')
        if not semester_id:
            return Response({'error': 'Semester ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        occurrences = course.occurrences.filter(semester_id=semester_id)
        serializer = CourseOccurrenceSerializerWithDetail(occurrences, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def degrees(self, request, pk=None):
        course = self.get_object()
        course_degrees = course.degrees.all()
        serializer = CourseDegreeSerializerWithDetail(course_degrees, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def dependencies(self, request, pk=None):
        course = self.get_object()
        course_dependencies = course.dependencies.all()
        required_courses = [cd.required_course for cd in course_dependencies]
        serializer = CourseSerializer(required_courses, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def dependent(self, request, pk=None):
        course = self.get_object()
        course_dependencies = course.dependent_courses.all()
        dependent_courses = [cd.course for cd in course_dependencies]
        serializer = CourseSerializer(dependent_courses, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def professors(self, request, pk=None):
        course = self.get_object
        professors = course.professors.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)

class CourseDegreeViewSet(viewsets.ModelViewSet):
    queryset = CourseDegree.objects.all()
    serializer_class = CourseDegreeSerializer
    permission_classes = [IsAuthenticated]

class CourseDependencyViewSet(viewsets.ModelViewSet):
    queryset = CourseDependency.objects.all()
    serializer_class = CourseDependencySerializer
    permission_classes = [IsAuthenticated]

class CourseOccurrenceViewSet(viewsets.ModelViewSet):
    queryset = CourseOccurrence.objects.all()
    serializer_class = CourseOccurrenceSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def enrollments(self, request, pk=None):
        course_occurrence = self.get_object()
        enrollments = course_occurrence.enrollments.all()
        serializer = CourseEnrollmentSerializerWithDetail(enrollments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def evaluations_list(self, request, pk=None):
        course_occurrence = self.get_object()
        evaluations_list = course_occurrence.evaluations_list.all()
        serializer = CourseOccurrenceEvaluationSerializer(evaluations_list, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def evaluations_results(self, request, pk=None):
        course_occurrence = self.get_object()
        evaluations_list = course_occurrence.evaluations_list.all()
        
        results_dict = defaultdict(lambda: {"evaluation": {}, "results": []})
        
        for evaluation in evaluations_list:
            evaluation_data = CourseOccurrenceEvaluationSerializer(evaluation).data
            
            results = []
            student_evaluations = evaluation.student_evaluations.all()
            for student_evaluation in student_evaluations:
                student_evaluation_data = {
                    "student_code": student_evaluation.student_code,
                    "marks_obtained": student_evaluation.obtained_marks
                }
                results.append(student_evaluation_data)
            
            results_dict[evaluation.id]["evaluation"] = evaluation_data
            results_dict[evaluation.id]["results"] = results
        
        results_dict = dict(results_dict)
        
        return Response(results_dict)
