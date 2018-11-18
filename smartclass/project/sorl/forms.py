from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationform(UserCreationForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
'''
    def save(self,commit=True):
        user=super(UserRegistrationform, self).save(commit=False)
        user.Firstname=cleaned_data['Firstname']
        user.Lastname=cleaned_data['Lastname']

        if commit:
            user.save()
'''
