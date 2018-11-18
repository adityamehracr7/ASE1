from rest_framework import serializers
from student_dash.models import examtype, table, studentattendence
from rest_framework import serializers

class studentattendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentattendence
        fields = ('attendence',)

class examtypeSerializer(serializers.ModelSerializer):
     #inheritence serializer
    class Meta:
        model = examtype
        fields = ('max_marks', 'exam_type',)

class tableSerializer(serializers.ModelSerializer):
    exam = examtypeSerializer()
    attendence = studentattendenceSerializer()
    class Meta:
        model = table
        fields = ('course_id', 'proff_id', 'student_id' ,'marks','student_name', 'exam', 'attendence',)


        
