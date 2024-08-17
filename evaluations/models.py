# evaluations/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from courses.models import CourseOccurrence
from enrollment.models import CourseEnrollment, DegreeEnrollment
from administration.models import Semester
from utils.dataClasses import GradeChoices

# all possible types of evaluations/assessments in a course. e.g., sessionals, end sem, quizzes ,projects etc.
class EvaluationType(models.Model):
    # DIRECTORY of Sessionals, Finals, Lab, Project, Quiz etc
    # The name of the evaluation type (e.g., "Midterm Exam", "Project").
    evaluation_type_name = models.CharField(max_length=100, unique=True)
    # Indicates if the evaluation is a group activity.
    is_group_activity = models.BooleanField(default=False)
    # The maximum score that can be obtained in this evaluation.
    max_score = models.PositiveIntegerField()

    def __str__(self):
        return self.evaluation_type_name

# An evaluation that occurs in a specific course occurrence.
class CourseOccurrenceEvaluation(models.Model):
    # Kis occurence ka evaluation hua h. e.g. CS101 ka sessional 1, CS101 ka final etc.
    # Foreign key to the CourseOccurrence model.
    course_occurrence = models.ForeignKey(CourseOccurrence, on_delete=models.PROTECT, related_name='evaluations_list')
    # Foreign key to the EvaluationType model.
    evaluation_type = models.ForeignKey(EvaluationType, on_delete=models.PROTECT, related_name='course_evaluations')
    # The date on which the evaluation is conducted.
    evaluation_date = models.DateField()
    def __str__(self):
        return str(self.id)

# The StudentEvaluation model represents the marks obtained by a student in a specific course evaluation.
class StudentEvaluation(models.Model):
    # Foreign key to the CourseOccurrenceEvaluation model.
    course_evaluation = models.ForeignKey(CourseOccurrenceEvaluation, on_delete=models.PROTECT, related_name='student_evaluations')
    # Foreign key to the CourseEnrollment model.
    course_enrollment = models.ForeignKey(CourseEnrollment, on_delete=models.PROTECT, related_name='student_evaluations')
    # The marks obtained by the student in this evaluation.
    obtained_marks = models.PositiveIntegerField()
    # Student code. BT id
    student_code = models.CharField(max_length=50, editable=False)

    def save(self, *args, **kwargs):
        # Fetch the student_code from the related CourseEnrollment object
        self.student_code = self.course_enrollment.degree_enrollment.student_code
        super().save(*args, **kwargs)

# Final grade of a student in a specific course.
class CourseGrades(models.Model):
    # One-to-one relationship with the CourseEnrollment model.
    course_enrollment = models.OneToOneField(CourseEnrollment, on_delete=models.PROTECT, related_name='grades')
    # The grade obtained by the student in the course, selected from predefined grade choices.
    grade = models.IntegerField(choices=GradeChoices)

# The grades obtained by a student in a specific semester.
class SemesterGrades(models.Model):
    # Foreign key to the DegreeEnrollment model.
    degree_enrollment = models.ForeignKey(DegreeEnrollment, on_delete=models.PROTECT, related_name='semester_grades')
    # The semester number (e.g., 1, 2, 3).
    semester_num = models.PositiveIntegerField()
    # Foreign key to the Semester model.
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT, related_name='grades')
    # The Semester Grade Point Average (SGPA) obtained by the student in this semester.
    sgpa = models.DecimalField(max_digits=4, decimal_places=2)

    def clean(self):
        # Get the degree associated with the degree enrollment.
        degree = self.degree_enrollment.degree
        # Ensure that the semester number is within the valid range for the degree.
        if self.semester_num < 1 or self.semester_num > degree.semesters:
            raise ValidationError(f"Semester must be between 1 and {degree.semesters} for the degree {degree.degree_code}")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
