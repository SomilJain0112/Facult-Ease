from django.contrib import admin
from .models import EvaluationType, StudentEvaluation, CourseOccurrenceEvaluation, SemesterGrades, CourseGrades

admin.site.register(EvaluationType)
admin.site.register(StudentEvaluation)
admin.site.register(CourseOccurrenceEvaluation)
admin.site.register(CourseGrades)
admin.site.register(SemesterGrades)
