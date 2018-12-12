from django import forms
from .models import StudentPost, Comment
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget



class BlogCreateForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    tags = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Add tags'}))
    class Meta:
        model = StudentPost
        fields = ('title','tags','body')



class UpdateBlog(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    tags = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Add tags'}))

    class Meta:
        model = StudentPost
        fields = ('title','tags','body')


class CommentsForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'django-textarea-comment','placeholder':'Write ur answer here !!!','rows':'10','cols':'70'}))
    class Meta:
        model = Comment
        fields =('content',)
