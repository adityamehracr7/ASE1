#from django.shortcuts import render
from .forms import *
from .models import table
from .models import faculty
from .models import course
from .models import examtype
from django.forms import modelformset_factory
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import table, examtype,student
from .serializers import tableSerializer



def is_faculty(user):
  try:
    if  faculty.objects.get(user = user):
        return True
  except:
        return False


def is_student(user):
   try:
     if  student.objects.get(user = user):
        return True
   except:
        return False






import os
import csv
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as new, logout as out,authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class Attendence_data(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
      tablelog= table.objects.all()
      serializer = tableSerializer(tablelog, many=True)
      return Response(serializer.data)

# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

# class tagsViewSet(viewsets.ModelViewSet):
#     queryset = table.objects.all()
#     serializer_class = tableSerializer

def prof_dashboard(request):
    if is_faculty(request.user):
        id = request.user.id
        proff = faculty.objects.get(user_id=id)
        proff_id = proff.id
        context={
            'name':request.user,
            'id':proff_id
        }
        return render(request, 'dc/dashboard.html/',context)
    else:
        return redirect('blog_list')









def simple_upload(request,course_id):
    #form = file_upload(request.POST, request.FILES)
    if request.method == 'POST':
        form = file_upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(request.FILES['fileupload'])
            create_table(str(request.FILES['fileupload']),request.user.id,course_id)
            messages.success(request,'uploaded successfuly');
            return redirect('teacher_page   ')

    else:
        form = file_upload()
        return render(request, 'fileindb/basic.html', {
        'form': form
    })

def create_table(file,id,course_id):
    path = 'media\static'

    c = open(path+'\\'+file,'r')
    data=[]
    q=c.readlines()
    a=q[0].split(",")
    for i in q:
        print(i)

        data.append(i.split(","))
    print(data)
    proff=faculty.objects.get(user_id=id)
    proff_id=proff.id


    size=int((len(data)))
    print(size)
    for j in range(size):
        print(data[j][0])
        exam=examtype.objects.get(course_id_id=course_id,exam_type=data[j][0]).id
        table.objects.create(exam_id=exam,student_id=data[j][1],student_name=data[j][2],marks=data[j][3],proff_id_id=proff_id,course_id_id=course_id)

def course_add(request):
    form1 = modelformset_factory(examtype, fields=('max_marks','exam_type'), extra=5)
    if request.method=='POST':
        form=add_course(request.POST or None)
        formset = form1(request.POST or None)
        if form.is_valid() and formset.is_valid():
            courses=form.save(commit=False)
            id=request.user.id
            proff = faculty.objects.get(user_id=id)
            proff_id = proff.id
            courses.proff_id_id=proff_id
            courses.save()
            for file in formset:
                if file.cleaned_data:
                    fiveform = examtype(course_id_id=request.POST['course_id'],max_marks=file.cleaned_data.get('max_marks'),exam_type=file.cleaned_data.get('exam_type'))
                    fiveform.save()
            context={
                'id':proff.id
            }
            return redirect('/teacher')


    else:
        form = add_course()
        formset = form1(queryset=examtype.objects.none())
    return render(request, 'fileindb/temp.html', {
        'form': form,
        'formset': formset,
    })


def add_exams(request,id):
    ur_courses=course.objects.filter(proff_id_id=id)
    if request.method=='POST':
        add_id=request.POST['cname']
        context={
            'add_id':add_id
        }
        return render(request,'fileindb/uploadcsv.html',context)

    context={
        'ur_courses':ur_courses
    }
    if ur_courses:
        return render(request,'fileindb/add_exam1.html',context)
    else:
        messages.success(request, "User Does't Exist . Create it first")
        return redirect('user_register')