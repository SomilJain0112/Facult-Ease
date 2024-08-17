from django.db import models
from utils.validators import validate_phone_number
from administration.models import Department

# The Professor model represents a faculty member (professor) in the institution.
class Professor(models.Model):
    professor_code = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    phone_number = models.CharField(validators=[validate_phone_number], max_length=18, blank=False)
    email_personal = models.EmailField(blank=False)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='professors')

    def __str__(self):
        return self.display_name or self.full_name

# The ProfessorCourse model represents the relationship between professors and the courses they teach.
class ProfessorCourse(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='courses')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='professors')

    class Meta:
        unique_together = ('professor', 'course')

    def __str__(self):
        return f"{self.professor.full_name} teaches {self.course.course_name}"
