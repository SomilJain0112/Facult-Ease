from django.contrib import admin
from .models import Degree, DegreeLevel, Department, Semester

admin.site.register(DegreeLevel)
admin.site.register(Department)
admin.site.register(Degree)
admin.site.register(Semester)