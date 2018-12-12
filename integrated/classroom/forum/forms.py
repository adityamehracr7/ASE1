from django import forms
from .models import TeacherPost, Comment
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


class PostCreateForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    tags = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Add tags'}))
    class Meta:
        model = TeacherPost
        fields = ('status','title','tags','body')



class UpdatePost(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    tags = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Add tags'}))

    class Meta:
        model = TeacherPost
        fields = ('status','title','tags','body')


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'django-textarea-comment','placeholder':'Write ur answer here !!!','rows':'10','cols':'70'}))
    class Meta:
        model = Comment
        fields =('content',)




class TeacherRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'UserName'}))
    first_name = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'FirstName'}))
    last_name = forms.CharField(max_length=30, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'LastName'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')




        if password1 != password2:

            self.add_error('password1', 'Password Did Not Match')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email id already exists')
        return email

class ProfessorLogin(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


class StudentRegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'UserName'}))
    first_name = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'FirstName'}))
    last_name = forms.CharField(max_length=30, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'LastName'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')




        if password1 != password2:

            self.add_error('password1', 'Password Did Not Match')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email id already exists')
        return email

