from django.contrib import admin
from .models import CourseEnrollment, DegreeEnrollment, Student, CourseStatus, DegreeStatus

admin.site.register(CourseStatus)
admin.site.register(DegreeStatus)
admin.site.register(Student)
admin.site.register(CourseEnrollment)
admin.site.register(DegreeEnrollment)
