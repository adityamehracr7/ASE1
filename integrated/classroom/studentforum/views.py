

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from fileindb.models import faculty,student
from django.core.mail import EmailMessage
import random
from django.contrib import messages



def is_faculty(user):
  try:
    if  faculty.objects.get(user = user):
        return True
  except:
        return False


def is_student(user):
    try:
        if student.objects.get(user = user):
            return True
    except:
        return False



def blog_create(request):
    if is_student(request.user):
        if request.method == 'POST':
            form1 = BlogCreateForm(request.POST)
            if form1.is_valid():
                post1 = form1.save(commit=False)
                post1.student = request.user
                post1.save()
                return redirect('blog_list')
        else:
            form1 = BlogCreateForm()
        contexts = {
            'form': form1,

        }
        return render(request, 'studentforum/post_create.html', contexts)
    else:
        messages.success(request,'You cannot create posts in students forum')
        return redirect('post_list')

def blog_edit(request, id):
    post = get_object_or_404(StudentPost, id=id)
    #ImageFormset = modelformset_factory(Images, fields=('image',), extra=3, max_num=8)

    if post.student != request.user:
        raise Http404()
    if request.method == 'POST':
        form = UpdateBlog(request.POST or None, instance=post)

        if form.is_valid() :
            form.save()
            return redirect('blog_list')
    else:
        form = UpdateBlog(instance=post)
    contexts = {
        'form': form,
        'post': post,

    }
    return render(request, 'studentforum/update_forum.html', contexts)


def blog_delete(request, id):
    post = get_object_or_404(StudentPost, id=id)
    if request.user != post.student:
        raise Http404()
    post.delete()
    return redirect('blog_list')


def blog_list(request):
    all_post = StudentPost.objects.all().order_by('created_time')
    context = {
        'all_post': all_post,
        'user': request.user.id
    }
    return render(request, 'studentforum/post_list.html', context)


def blog_detail(request, id):
    post = get_object_or_404(StudentPost, id=id)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

    comment_form = CommentsForm()
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comm = None
            if reply_id:
                comm = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comm)
            comment.save()
            comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
            comm_form = CommentsForm()
            contexts = {
                'post': post,
                'comments': comments,
                'comment_form': comm_form,
            }

            return render(request, 'studentforum/details.html', contexts)

        else:
            comment_form = CommentsForm()
    contexts = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'studentforum/details.html', contexts)


def comments_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('blog_list')



def user_post_list(request):
    post_list_user = StudentPost.objects.filter(student=request.user)
    contexts = {
        'post_list_user':post_list_user,
    }
    return render(request,'studentforum/user_post_list.html', contexts)
