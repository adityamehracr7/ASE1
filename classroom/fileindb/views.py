#from django.shortcuts import render
from .forms import *
from .models import table
from .models import faculty
from .models import course
from .models import examtype
import os
import csv
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as new, logout as out,authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage



def simple_upload(request,course_id):
    #form = file_upload(request.POST, request.FILES)
    if request.method == 'POST':
        form = file_upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(request.FILES['fileupload'])
            create_table(str(request.FILES['fileupload']),request.user.id,course_id)
            return HttpResponse('uploded')

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
        table.objects.create(student_id=data[j][0],student_name=data[j][1],marks=data[j][2],exam_id=data[j][3],proff_id_id=proff_id,course_id_id=course_id)

def course_add(request):
    if request.method=='POST':
        form=add_course(request.POST or None)
        if form.is_valid():
            courses=form.save(commit=False)
            id=request.user.id
            proff = faculty.objects.get(user_id=id)
            proff_id = proff.id
            courses.proff_id_id=proff_id
            courses.save()

    else:
        form = add_course()
    return render(request, 'fileindb/take_course.html', {
        'form': form
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

    return render(request,'fileindb/add_exam.html',context)


