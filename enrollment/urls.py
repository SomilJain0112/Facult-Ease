# enrollment/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DegreeStatusViewSet, CourseStatusViewSet, StudentViewSet, DegreeEnrollmentViewSet, CourseEnrollmentViewSet

router = DefaultRouter()
router.register(r'degree_statuses', DegreeStatusViewSet)
router.register(r'course_statuses', CourseStatusViewSet)
router.register(r'students', StudentViewSet)
router.register(r'degree_enrollments', DegreeEnrollmentViewSet)
router.register(r'course_enrollments', CourseEnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
