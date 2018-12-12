from django import forms
from .models import file,course,faculty,examtype


class file_upload(forms.ModelForm):
    class Meta:
        model = file
        fields=('fileupload',)


class add_course(forms.ModelForm):
    class Meta:
        model=course
        fields=('course_id','course_name',)


class examtype_add(forms.ModelForm):
    class Meta:
        model=examtype
        fields=('max_marks','exam_type')

