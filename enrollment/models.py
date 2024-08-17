# enrollment/models.py
from django.db import models
from django.core.exceptions import ValidationError
from utils.validators import validate_phone_number, validate_year
from administration.models import Degree
from courses.models import CourseOccurrence

# DegreeStatus is a model that stores the status of a degree. e.g. Active, Inactive, Graduated etc.
# The possible statuses for a student's degree enrollment.
class DegreeStatus(models.Model):
    # A unique code representing the status (e.g., "Enrolled", "Graduated", "Withdrawn").
    status_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.status_code

# CourseStatus is a model that stores the status of a course. e.g. Enrolled, Dropped, Completed etc.
# The possible statuses for a student's course enrollment.
class CourseStatus(models.Model):
    # A unique code representing the status (e.g., "Completed", "In Progress", "Dropped").
    status_code = models.CharField(max_length=50)

    def __str__(self):
        return self.status_code

# The represents a student in the system.
class Student(models.Model):
    # Full name of the student.
    student_name = models.CharField(max_length=255)
    # Email address of the student.
    student_email = models.EmailField()
    # Phone number of the student, validated by a custom validator.
    student_phone = models.CharField(validators=[validate_phone_number], max_length=18, blank=False)
    # Date of birth of the student.
    date_of_birth = models.DateField()
    # ID is invisible, but have faith it is there. 
    def __str__(self):
        return self.student_name


# Konsi branch mein konse bacche h in which year.
# CGPA and SGPA ka histroy ka alg se table banegi. Can ignore for now. Nice to have to analyse performance of students.
# The student's enrollment in a degree program.
class DegreeEnrollment(models.Model):
    # Foreign key to the Student model.
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='degree_enrollments')
    # Foreign key to the Degree model.
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT, related_name='enrollments')
    # A unique code assigned to the student for the degree program. ( BT ID )
    student_code = models.CharField(max_length=50, unique=True)
    # Foreign key to the DegreeStatus model.
    degree_status = models.ForeignKey(DegreeStatus, on_delete=models.PROTECT, related_name='degree_enrollments')
    # Date of enrollment in the degree program.
    enrollment_date = models.DateField()
    # Batch year of the student (e.g., 2024), validated by a custom validator.
    batch = models.CharField(max_length=4, validators=[validate_year])
    # Cumulative Grade Point Average (CGPA) of the student.
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=None)

    def __str__(self):
        return f"Degree Enrollment {self.id}"

# Konsa course kis student ne liya h. Bap of course of occurence.
# The student's enrollment in a specific course occurrence.
class CourseEnrollment(models.Model):
    # Foreign key to the DegreeEnrollment model.
    degree_enrollment = models.ForeignKey(DegreeEnrollment, on_delete=models.PROTECT, related_name='course_enrollments')
    # Foreign key to the CourseOccurrence model.
    course_occurrence = models.ForeignKey(CourseOccurrence, on_delete=models.PROTECT, related_name='enrollments')
    # Foreign key to the CourseStatus model.
    course_status = models.ForeignKey(CourseStatus, on_delete=models.PROTECT, related_name='course_enrollments')
    # The semester number in which the course is taken.
    semester_number = models.PositiveIntegerField()

    class Meta:
        # Ensure that each degree enrollment can only enroll in a specific course occurrence once.
        unique_together = ('degree_enrollment', 'course_occurrence')

    def __str__(self):
        return f"Course Enrollment {self.id}"
