from django.contrib import admin
from .models import Course, CourseDegree, CourseDependency, CourseOccurrence

admin.site.register(CourseDegree)
admin.site.register(CourseDependency)
admin.site.register(Course)
admin.site.register(CourseOccurrence)
