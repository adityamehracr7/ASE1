
from django.shortcuts import render, get_object_or_404, redirect
from .models import Images
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse , Http404
from django.forms import modelformset_factory


from fileindb.models import faculty





def user_register(request):
    if request.method == 'POST':
        form = ProfessorRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            faculty.objects.create(user=new_user,proff_name=request.POST['username'])
            return redirect('user_login')
    else:
        form = ProfessorRegistration()
    contexts = {
        'form':form
    }
    return render(request, 'forum/register.html', contexts)



def user_login(request):
    if request.method == 'POST':
        form = ProfessorLogin(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('you are now logged in')

                else:
                    return HttpResponse('User is not active')

            else:
                return HttpResponse('User is not available')

    else:
        form = ProfessorLogin()
        contexts={'form':form}

    return render(request,'forum/login.html', contexts)


def user_logout(request):
    logout(request)
    return redirect('index')


def index (request):
    return HttpResponse('you are out')    #post_list


def post_create(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=3)

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.teacher = request.user
            post.save()

            for file in formset:
                if file.cleaned_data:
                    try:
                        photo = Images(post=post,image=file.cleaned_data.get('image'))
                        photo.save()
                    except Exception as e:
                        break

            return redirect('post_list')
    else:
        form = PostCreateForm()
        formset = ImageFormset(queryset=Images.objects.none())
    contexts = {
        'form':form,
        'formset':formset,

    }
    return render(request, 'forum/post_create.html', contexts)





def post_edit(request, id):
    post = get_object_or_404(TeacherPost,id=id)
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=3 , max_num=8)


    if post.teacher != request.user:
        raise Http404()
    if request.method == 'POST':
        form = UpdatePost(request.POST or None, instance=post)
        formset = ImageFormset(request.POST or None, request.FILES or None)

        if form.is_valid() and formset.is_valid():
            form.save()
            data = Images.objects.filter(post=post)
            for index,f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:   # Previously not saved
                        photo = Images(post=post, image=f.cleaned_data.get('image'))
                        photo.save()
                    elif f.cleaned_data['image'] is False:
                        photo = Images.objects.get(id=request.POST.get('form-' + str(index) + '-id'))
                        photo.delete()
                    else:
                        photo = Images(post=post, image=f.cleaned_data.get('image'))
                        temp = Images.objects.get(id=data[index].id)
                        temp.image = photo.image
                        temp.save()

            return redirect('post_list')
    else:
        form = UpdatePost(instance=post)
        formset = ImageFormset(queryset=Images.objects.filter(post=post)) # This formset will give already uploaded images
    contexts = {
        'form':form,
        'post':post,
        'formset':formset,

    }
    return render(request, 'forum/update_forum.html', contexts)



def post_delete(request,id):
    post = get_object_or_404(TeacherPost,id=id)
    if request.user != post.teacher:
        raise Http404()
    post.delete()
    return redirect('post_list')



def post_list(request):
    all_post=TeacherPost.objects.filter(status='publish').order_by('created_time')
    context={
        'all_post':all_post,
        'user':request.user.id
    }
    return render(request,'forum/post_list.html',context)


def post_detail(request,id):
    post = get_object_or_404(TeacherPost, id=id)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comm = None
            if reply_id:
                comm = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comm)
            comment.save()
            comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
            comm_form=CommentForm()
            contexts = {
                'post': post,
                'comments': comments,
                'comment_form': comm_form,
            }

            return render(request, 'forum/details.html', contexts)

        else:
            comment_form = CommentForm()
    contexts = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'forum/details.html', contexts)




def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('post_list')












