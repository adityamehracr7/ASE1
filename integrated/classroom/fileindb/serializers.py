from rest_framework import serializers
from .models import examtype, table
from rest_framework import serializers



class examtypeSerializer(serializers.ModelSerializer):
     #inheritence serializer
    class Meta:
        model = examtype
        fields = ('max_marks', 'exam_type',)

class tableSerializer(serializers.ModelSerializer):
    exam = examtypeSerializer()

    
    class Meta:
        model = table
        fields = ('course_id', 'proff_id', 'student_id' ,'marks','student_name', 'exam',)


        
