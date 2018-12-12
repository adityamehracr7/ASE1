
from django.shortcuts import render, get_object_or_404, redirect
from .models import Images,notifications
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse , Http404,JsonResponse
from django.forms import modelformset_factory
from django.db.models import Q
from django.template.loader import render_to_string
from fileindb.models import faculty
from django.contrib import messages
from .models import  otp_verify
from .forms import *
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from fileindb.models import faculty,student
from django.core.mail import EmailMessage
import random
from django.contrib import messages



def home(request):
    return render(request,'forum/home.html')

def teacher_page(request):
    if is_faculty(request.user):
        id = request.user.id
        proff = faculty.objects.get(user_id=id)
        proff_id = proff.id
        context={
            'name':request.user,
            'id':proff_id
        }
        return render(request, 'forum/home page.html',context)
    else:
        return redirect('home')


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
                    if is_student(request.user):
                        return redirect('blog_list')
                    else:
                        return redirect('/teacher')

                else:
                    return HttpResponse('User is not active')

            else:
                return HttpResponse('User is not available')

    else:
        form = ProfessorLogin()
    contexts={'form':form}

    return render(request,'forum/newlogin.html', contexts)


def user_logout(request):
    logout(request)
    return redirect('user_login')



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
        formset = ImageFormset(queryset=Images.objects.filter(post=post))
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
    if is_faculty(request.user):
        all_post=TeacherPost.objects.filter(status='publish').order_by('created_time').order_by('-id')

        query = request.GET.get('q')
        if query:
            all_post = TeacherPost.objects.filter(status='publish').filter(
                Q(title__icontains=query) |
                Q(teacher__username__iexact=query)
            )

        user_likes = 0

        if request.user.is_authenticated:
            #get_user = get_object_or_404(User, id=request.user.id)
            post_list_user = TeacherPost.objects.filter(teacher=request.user)
            for post in post_list_user:
                num = post.total_likes()
                user_likes += num

        context={
            'all_post':all_post,
            'user_likes': user_likes,


        }
        return render(request,'forum/post_list.html',context)
    else:

        return redirect('blog_list')


def post_detail(request,id):
    post = get_object_or_404(TeacherPost, id=id)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')


    is_liked = False
    is_disliked = False
    if post.likes.filter(id=request.user.id):
        is_liked = True
        print('It is liked')
    elif post.dislikes.filter(id=request.user.id):
        is_disliked = True
        print("IT is disliked")
    else:
        print("This can't Happen")

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
            notf=notifications.objects.create(com_id=comment,user=request.user)
            notf.save()
            comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
            comm_form=CommentForm()
            contexts = {
                'post': post,
                'comments': comments,
                'comment_form': comm_form,
                'total_likes': post.total_likes(),
                'total_dislikes': post.total_dislikes(),
                'is_liked': is_liked,
                'is_disliked': is_disliked,


            }

            return render(request, 'forum/details.html', contexts)

        else:
            comment_form = CommentForm()
    contexts = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'is_disliked':is_disliked,
        'total_likes': post.total_likes(),
        'total_dislikes': post.total_dislikes(),
        

    }

    return render(request, 'forum/details.html', contexts)




def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('post_list')


def like_post(request):
    post = get_object_or_404(TeacherPost,id=request.POST.get('id'))
    is_liked = False
    is_disliked = False
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
        post.likes.add(request.user)
        is_liked = True
    elif post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
        print('THIS SHOULD BE')
    contexts = {
        'post': post,
        'is_liked':is_liked,
        'is_disliked':is_disliked,
        'total_likes':post.total_likes(),
        'total_dislikes':post.total_dislikes(),
    }
    if request.is_ajax():
        html = render_to_string('forum/likes.html', contexts, request=request)
        return JsonResponse({'form':html})


def dislike_post(request):
    post = get_object_or_404(TeacherPost, id=request.POST.get('id'))
    is_disliked = False
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post.dislikes.add(request.user)
        is_disliked = True
    elif post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
        is_disliked = False
    else:
        post.dislikes.add(request.user)
        is_disliked = True

    contexts = {
        'post': post,
        'is_disliked':is_disliked,
        'is_liked':is_liked,
        'total_dislikes':post.total_dislikes(),
        'total_likes':post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('forum/likes.html', contexts, request=request)
        return JsonResponse({'form':html})





def user_post_list(request):
    post_list_user = TeacherPost.objects.filter(teacher=request.user)
    contexts = {
        'post_list_user':post_list_user,
    }
    return render(request,'forum/user_post_list.html', contexts)


def user_notifs(request):
    notf = notifications.objects.filter(com_id__in=Comment.objects.filter(post__in=TeacherPost.objects.filter(teacher=request.user))).order_by('-id').values()

    A=[]
    count=0
    for notif in notf:
        B=[]
        user = User.objects.get(id=notif['user_id'])
        username=user.username
        com = Comment.objects.get(id=notif['com_id_id'])
        mypost_id = com.post_id
        post=TeacherPost.objects.get(id=mypost_id)
        title=post.title
        B.append(notif)
        B.append(username)
        B.append(title)
        A.append(B)

        if notif['is_read'] == 0:
            count = count+1


    context={
        'notf':A,
        'count':count
    }
    print(A)
    print(count)
    obj = notifications.objects.all()
    for each in obj:
        each.is_read = True
        each.save()

    return render(request,'forum/notif.html',context)





def send(mail,user):
    global otp
    otp = random.randint(10000,99999)
    mail = EmailMessage('Email verification','Hi '+user+', welcome to smartclass ,your otp is'+str(otp), to=[mail])
    mail.send()
    #send_mail('hi welcome to smartclass ,otp is:',str(otp),'smartclasstracking@gmail.com',[mail])
    print("otp = ",otp)
    return otp


def send1(mail):
    global otp
    otp = random.randint(10000,99999)
    mail = EmailMessage('Email verification,',' welcome to smartclass ,your otp is'+str(otp), to=[mail])
    mail.send()
    #send_mail('hi welcome to smartclass ,otp is:',str(otp),'smartclasstracking@gmail.com',[mail])
    print("otp = ",otp)
    return otp


def register(request):
    form = TeacherRegistrationForm()
    form1 = StudentRegistrationForm()
    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'forum/Tea_Stud_register.html', context)


def student_register(request):
    form = TeacherRegistrationForm(None)
    form1 = StudentRegistrationForm(request.POST or None)

    if request.method == 'POST':

        if form1.is_valid():
            email = form1.data['email']
            otp1 = send(email,form1.data['username'])
            # new_user = form1.save(commit=False)
            firstname = form1.data['first_name']
            lastname = form1.data['last_name']
            username = form1.data['username']
            password1 = form1.data['password1']
            password2 = form1.data['password2']
            try:
                user1 = otp_verify.objects.get(name=username)
                user1.otp = otp1
                user1.save()
            except:
                user_otp = otp_verify.objects.create(name=username, otp=otp1)
                user_otp.save()
            context = {
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'email': email,
                'password1': password1,
                'password2': password2,
            }
            return render(request, 'forum/verify.html', context)
    else:
        form = TeacherRegistrationForm()
        form1 = StudentRegistrationForm()

    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'forum/Tea_Stud_register.html', context)


def verify(request):
    if request.method == 'POST':
        otp1 = request.POST.get('typed_otp')
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        otp2 = otp_verify.objects.get(name=username).otp
        print("otp2 is ",otp2)
        if otp1 == str(otp2):
            new_user = User.objects.create(username=username, email=email, first_name=firstname, last_name=lastname)
            new_user.set_password(request.POST['password1'])
            new_student = student(user=new_user,stud_name=firstname)
            new_user.save()
            new_student.save()
            return redirect('user_login')
        else:
            context = {
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'email': email,
                'password1': password1,
                'password2': password2,
            }
            messages.error(request, 'wrong otp')
            return render(request, 'forum/verify.html', context)
    else:
        return HttpResponse('wrong way')


def teacher_register(request):
    form = TeacherRegistrationForm(request.POST or None)
    form1 = StudentRegistrationForm()
    if request.method == 'POST':

        if form.is_valid():
            email = form.data['email']
            otp1 = send(email,form.data['username'])
            firstname = form.data['first_name']
            lastname = form.data['last_name']
            username = form.data['username']
            password1 = form.data['password1']
            password2 = form.data['password2']
            try:
                user = otp_verify.objects.get(name=username)
                user.otp = otp1
                user.save()
            except:
                user_otp = otp_verify.objects.create(name=username, otp=otp1)
                user_otp.save()
            context = {
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'email': email,
                'password1': password1,
                'password2': password2,
            }
            return render(request, 'forum/verify2.html', context)
    else:
        form = TeacherRegistrationForm()
        form1 = StudentRegistrationForm()

    context = {
        'form1': form1,
        'form': form
    }
    return render(request, 'forum/Tea_Stud_register.html',context)


def verify2(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        otp1 = request.POST.get('typed_otp')
        otp2 = otp_verify.objects.get(name=username).otp
        if otp1 == str(otp2):
            new_user1 = User.objects.create(username=username, email=email, first_name=firstname, last_name=lastname)
            new_user1.set_password(request.POST['password1'])
            new_teacher = faculty(user= new_user1,proff_name=firstname)
            new_user1.save()
            new_teacher.save()
            return redirect('user_login')
        else:
            context = {
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'email': email,
                'password1': password1,
                'password2': password2,
            }
            messages.error(request, 'wrong otp')
            return render(request, 'forum/verify2.html', context)
    else:
        return HttpResponse('wrong way')


def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        reset_otp = send1(email)
        try:
            username = User.objects.get(email=email).username
        except:
            messages.error(request, 'no user exists with this email')
            return render(request, 'forum/forget_pass.html')

        try:
            user = otp_verify.objects.get(name=username)
            user.otp = reset_otp
            user.save()
        except:
            user_otp = otp_verify.objects.create(name=username, otp=reset_otp)
            user_otp.save()
        return render(request, 'forum/forget_otp.html', {'email': email})
    else:
        return render(request, 'forum/forget_pass.html')


def forget_otp_verification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = User.objects.get(email=email).username
        new_otp = otp_verify.objects.get(name=username).otp
        otp1 = request.POST.get('otp1')
        if otp1 == str(new_otp):
            return render(request, 'forum/reset_password.html', {'email': email})
        else:
            messages.error(request, 'incorrect otp')
            return render(request, 'forum/forget_otp.html', {'email': email})
    else:
        return render(request, 'forum/forget_otp.html')


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = User.objects.get(email=email).username
        user = User.objects.get(username=username)
        reset1 = request.POST['resetpass1']
        reset2 = request.POST['resetpass2']
        if reset1 != reset2:
            messages.error(request, 'passwords didnot match')
            return render(request, 'forum/forget_pass.html', {'email': email})
        if len(reset1) < 8:
            messages.error(request, 'password is too short')
            return render(request, 'forum/forget_pass.html', {'email': email})
        user.set_password(reset1)
        user.save()
        return redirect('user_login')
    else:
        return render(request, 'forum/forget_pass.html')

