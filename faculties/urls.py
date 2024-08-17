from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessorViewSet, ProfessorCourseViewSet

router = DefaultRouter()
router.register(r'professors', ProfessorViewSet)
router.register(r'professor_courses', ProfessorCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
