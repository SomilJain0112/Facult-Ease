# courses/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from administration.models import Department, Degree, Semester
from faculties.models import ProfessorCourse
from utils.validators import validate_phone_number, validate_year

# The specific courses offered by a department.
class Course(models.Model):
    # Full name of the course (e.g., Data Structures and Algorithms).
    course_name = models.CharField(max_length=200, unique=True)
    # Unique code for the course (e.g., CS101).
    course_code = models.CharField(max_length=20, unique=True)
    # Indicates if the course has a lab component.
    has_lab = models.BooleanField(default=False)
    # The grade points associated with the course.
    credits = models.PositiveIntegerField()
    # Foreign key to the Department model indicating the department offering this course.
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='courses')

    def __str__(self):
        return self.course_code

# Th        e relationship between courses and degrees. Which Courses are taught in which degree and in which semester.
class CourseDegree(models.Model):
    # Foreign key to the Course model.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='degrees')
    # Foreign key to the Degree model.
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='courses')
    # The semester number of the degree in which the course is offered.
    semester_num = models.PositiveSmallIntegerField()
    # The slot in which the course is offered (e.g., A, B, C).
    slot = models.CharField(max_length=1)
    batch = models.CharField(max_length=4, validators=[validate_year])
    type = models.CharField(max_length=4)
    l = models.PositiveSmallIntegerField()
    t = models.PositiveSmallIntegerField()
    p = models.PositiveSmallIntegerField()

    class Meta:
        # Ensure that a professor can be assigned to teach a course only once.
        unique_together = ('degree', 'course', 'semester_num')

# Prerequisite relationships between courses.
'''class CourseDependency(models.Model):
    # the course that has a prerequisite.
    course = models.ForeignKey(Course, related_name='dependencies', on_delete=models.CASCADE)
    # the required prerequisite course.
    required_course = models.ForeignKey(Course, related_name='dependent_courses', on_delete=models.PROTECT)
    def __str__(self):
        return f"Course {self.course.course_code} requires {self.required_course.course_code}"
    
    from django.db import models'''

class CourseDependency(models.Model):
    # the course that has a prerequisite.
    course = models.ForeignKey(Course, related_name='dependencies', on_delete=models.CASCADE)
    # the required prerequisite course.
    required_course = models.ForeignKey(Course, related_name='dependent_courses', on_delete=models.PROTECT)

    def __str__(self):
        return f"Course {self.course.course_code} requires {self.required_course.course_code}"


# The CourseOccurrence model represents a specific instance of a course being offered in a semester.
# Different sections and subsections are also repretesnted by occurrenses
class CourseOccurrence(models.Model):
    # Indicates if the occurrence is for a lab component.
    is_lab = models.BooleanField(default=False)
    # The maximum number of students that can enroll in this course occurrence.
    capacity = models.PositiveSmallIntegerField()

    # Foreign key to the Course model.
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='occurrences')
    # Foreign key to the professor teaching this course.
    professor = models.ForeignKey('faculties.Professor', on_delete=models.PROTECT, related_name='course_occurrences')
    # Foreign key to the assistant professor, if any.
    assistant_professor = models.ForeignKey(
        'faculties.Professor', 
        on_delete=models.SET_NULL, 
        related_name='assistant_course_occurrences', 
        null=True, 
        blank=True
    )
    # The institutional level semester in which this course occurrence is running.
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT, related_name='course_occurrences')
    is_active = models.BooleanField(default=True)
    # Custom validation to ensure the assigned professor teaches the selected course.
    def clean(self):
        if not ProfessorCourse.objects.filter(professor=self.professor, course=self.course).exists():
            raise ValidationError('Assigned professor does not teach the selected course.')

    def save(self, *args, **kwargs):
        # Call full_clean to enforce the custom validation before saving.
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Course Occurrence {self.id} for course {self.course.course_code}"
