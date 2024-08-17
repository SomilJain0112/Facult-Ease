# evaluations/serializers.py
from rest_framework import serializers
from .models import EvaluationType, CourseOccurrenceEvaluation, StudentEvaluation, CourseGrades, SemesterGrades

class EvaluationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationType
        fields = '__all__'

class CourseOccurrenceEvaluationSerializer(serializers.ModelSerializer):
    evaluation_type_name = serializers.CharField(source='evaluation_type.evaluation_type_name', read_only=True)
    is_group_activity = serializers.BooleanField(source='evaluation_type.is_group_activity', read_only=True)
    max_score = serializers.IntegerField(source='evaluation_type.max_score', read_only=True)
    class Meta:
        model = CourseOccurrenceEvaluation
        fields = '__all__'

class StudentEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEvaluation
        fields = '__all__'

class CourseGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseGrades
        fields = '__all__'

class SemesterGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterGrades
        fields = '__all__'
