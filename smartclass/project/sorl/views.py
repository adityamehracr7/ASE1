from django.shortcuts import render,redirect
from sorl.forms import UserRegistrationform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('forumhome')
    else:
        if request.method == 'POST':
            form = UserRegistrationform(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request,f'user created successfully,you can now login')
                return redirect('login')
        else:
            form=UserRegistrationform()

        return render(request,'sorl/signup.html',{'form':form})

@login_required
def profile(request):
    return render(request,'sorl/profile.html')
