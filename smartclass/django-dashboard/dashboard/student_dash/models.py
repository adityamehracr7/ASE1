from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

Exam_Type = {
    ('mid1', 'MID1'),
    ('mid2', 'MID2'),
    ('project', 'PROJECT'),
    ('lab', 'LAB'),
    ('end', 'END'),
}

class file(models.Model):
    fileupload=models.FileField(upload_to='static', validators=[FileExtensionValidator(['csv'])],unique=None)


class faculty (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #proff_id=models.AutoField(primary_key=True,blank=True)
    proff_name=models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_id)


class course(models.Model):
    course_id=models.CharField(max_length=50,primary_key=True,unique=True)
    course_name=models.CharField(max_length=100)
    proff_id=models.ForeignKey(faculty,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course_name)

class examtype(models.Model):
    exam_type = models.CharField(max_length=20, choices=Exam_Type, default='mid1')
    max_marks=models.CharField(max_length=50)
    course_id=models.ForeignKey(course,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class studentattendence(models.Model):
    attendence = models.CharField(max_length=100)
   
    def __str__(self):
        return str(self.attendence)

class table(models.Model):
    student_id=models.CharField(max_length=100)
    student_name=models.CharField(max_length=100)
    proff_id=models.ForeignKey(faculty,on_delete=models.CASCADE)
    course_id=models.ForeignKey('course',on_delete=models.CASCADE)
    marks=models.CharField(max_length=250)
    exam=models.ForeignKey(examtype,on_delete=models.CASCADE)
    attendence = models.ForeignKey(studentattendence , on_delete=models.CASCADE)
    def __str__(self):
        return str(self.proff_id)+' '+'table'






