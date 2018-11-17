from django.db import models
from django.core.validators import FileExtensionValidator

class file(models.Model):
    fileupload=models.FileField(upload_to='static', validators=[FileExtensionValidator(['csv'])])


class faculty (models.Model):
    proff_id=models.CharField(max_length=100,primary_key=True,unique=True)
    proff_name=models.CharField(max_length=100)


class course(models.Model):
    course_id=models.CharField(max_length=50,primary_key=True,unique=True)
    course_name=models.CharField(max_length=100)
    proff_id=models.ForeignKey(faculty,on_delete=models.CASCADE)

class examtype(models.Model):
    max_marks=models.CharField(max_length=50)
    course_id=models.ForeignKey(course,on_delete=models.CASCADE)

class table(models.Model):
    student_id=models.CharField(max_length=100,primary_key=True,unique=True)
    student_name=models.CharField(max_length=100)
    proff_id=models.ForeignKey('faculty',on_delete=models.CASCADE)
    course_id=models.ForeignKey('course',on_delete=models.CASCADE)
    marks=models.FloatField()
    exam=models.ForeignKey(examtype,on_delete=models.CASCADE)






