from rest_framework import serializers
from .models import Department, DegreeLevel, Semester, Degree

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DegreeLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeLevel
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class DegreeSerializer(serializers.ModelSerializer):

    degree_level_code = serializers.CharField(source='degree_level.level_code', read_only=True)
    department_code = serializers.CharField(source='department.department_code',read_only=True)
    class Meta:
        model = Degree
        fields = '__all__'
