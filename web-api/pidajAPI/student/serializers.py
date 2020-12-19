from .models import Student, Grade
from rest_framework import serializers

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'student_id', 'course', 'value']

#    def to_representation(self, instance):
#        self.fields['student'] =  StudentSerializer(read_only=True)
#        return super(GradeSerializer, self).to_representation(instance)  

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    grades = GradeSerializer(many=True, read_only=True, source='grade_set')
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'index_number', 'email', 'grades']    