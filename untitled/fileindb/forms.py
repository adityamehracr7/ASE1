from django import forms
from .models import file

class file_upload(forms.ModelForm):
    class Meta:
        model = file
        fields=('fileupload',)