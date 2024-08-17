# courses/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CourseDegreeViewSet, CourseDependencyViewSet, CourseOccurrenceViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'coursedegrees', CourseDegreeViewSet)
router.register(r'coursedependencies', CourseDependencyViewSet)
router.register(r'courseoccurrences', CourseOccurrenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
