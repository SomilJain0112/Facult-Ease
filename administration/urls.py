# administration/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, DegreeLevelViewSet, SemesterViewSet, DegreeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'degreelevels', DegreeLevelViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'degrees', DegreeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]