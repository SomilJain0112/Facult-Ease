# administration/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from utils.validators import validate_year

# Departments within the institution. (e.g., CSE, ECE, Basic Science)
class Department(models.Model):
    # Name of the department (e.g., Electronics & Communication Engg.)
    department_name = models.CharField(max_length=100, unique=True)
    # Unique code for the department (e.g., CSE, ECE)
    department_code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.department_code

# Different levels of degrees (e.g., Bachelor, Master, PHD).
class DegreeLevel(models.Model):
    # Full name of the degree level (e.g., Bachelor's, Master's).
    level_name = models.CharField(max_length=150, unique=True)
    # Short code for the degree level (e.g., BSc, MSc).
    level_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.level_code

# Institutional level representation of an academic semester within a particular year.
# Some semester (1st, 3rd, 5th etc) of each batch will be running in this Semester.  
class Semester(models.Model):
    # Running year of the semester (e.g., 2023, 2024).
    year = models.CharField(max_length=4, validators=[validate_year])
    # Start date of the semester.
    start_date = models.DateField()
    # End date of the semester.
    end_date = models.DateField()
    # Indicates if the semester is odd (True) or even (False).
    is_odd = models.BooleanField()

    # Custom validation to ensure the start date is before the end date.
    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError(_('End date must be after start date'))

# The Degree model represents a specific academic degree (e.g., B.Tech. Computer Science & Engineering, B. Tech. ECE (Internet of Things)).
class Degree(models.Model):
    # Full name of the degree (e.g., Bachelor of Science in Computer Science).
    degree_name = models.CharField(max_length=200, unique=True)
    # Unique code for the degree (e.g., 4110).
    degree_code = models.CharField(max_length=20, unique=True)
    # Duration of the degree program.
    duration_years = models.PositiveSmallIntegerField(default=4)
    duration_months = models.PositiveSmallIntegerField(default=0)
    # Number of credits required to complete the degree.
    credits_required = models.PositiveSmallIntegerField()
    # Number of semesters required to complete the degree.
    semesters = models.PositiveSmallIntegerField()
    # Foreign key to the DegreeLevel model indicating the level of this degree.
    degree_level = models.ForeignKey(DegreeLevel, on_delete=models.PROTECT, related_name='degrees')
    # Foreign key to the Department model indicating the department offering this degree.
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='degrees')

    def __str__(self):
        return self.degree_code
