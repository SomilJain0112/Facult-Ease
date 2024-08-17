# evaluations/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluationTypeViewSet, CourseOccurrenceEvaluationViewSet, StudentEvaluationViewSet, CourseGradesViewSet, SemesterGradesViewSet

router = DefaultRouter()
router.register(r'evaluation_types', EvaluationTypeViewSet)
router.register(r'course_occurrence_evaluations', CourseOccurrenceEvaluationViewSet)
router.register(r'student_evaluations', StudentEvaluationViewSet)
router.register(r'course_grades', CourseGradesViewSet)
router.register(r'semester_grades', SemesterGradesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
