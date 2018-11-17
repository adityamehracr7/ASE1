from django import forms
from .models import TeacherPost, Comment
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget



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



class ProfessorRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder':'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder':'Confirm password'}))
    username = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'last_name'}))
    email = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'email'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email Already Registered')
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password did not match')
        return confirm_password


class ProfessorLogin(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs = {'placeholder':'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs = {'placeholder':'password'}))
