#from django.shortcuts import render
from .forms import file_upload
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



def profile(request):
    if request.method == "POST":
        course_id = request.POST['cid']
        course_name = request.POST['cname']
        course.objects.create(course_id = course_id, course_name = course_name)
        return HttpResponse("saved")
    else:
        return render(request, 'fileindb/take_course.html')

    return HttpResponse("not saved")


def simple_upload(request):
    #form = file_upload(request.POST, request.FILES)
    if request.method == 'POST':
        form = file_upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(request.FILES['fileupload'])
            create_table(str(request.FILES['fileupload']))
            return HttpResponse('uploded')

    else:
        form = file_upload()
        return render(request, 'fileindb/basic.html', {
        'form': form
    })

def create_table(file):
    path = 'media\static'

    c = open(path+'\\'+file,'r')
    data=[]
    q=c.readlines()
    a=q[0].split(",")
    for i in q:
        print(i)

        data.append(i.split(","))
    print(data)

    proff_id=1
    course_id='ase1'

    size=int((len(data)))
    print(size)
    for j in range(size):
        table.objects.create(student_id=data[j][0],student_name=data[j][1],marks=data[j][2],exam_id=data[j][3],proff_id_id=proff_id,course_id_id=course_id)








