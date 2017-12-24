from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ToDoCreate(forms.Form):
    title = forms.CharField(required=True,label='' ,widget=forms.TextInput(attrs={'id':'entry'}))
    content = forms.CharField(required=True, label='', widget=forms.Textarea(attrs={'id':'content','style':'resize:none'}))

class SignUp(UserCreationForm):
    username=forms.CharField(required=True,label='Username',)
    password1=forms.CharField(required=True, label='Password',min_length=8, widget=forms.TextInput(attrs={'type':'password'}))
    password2=forms.CharField(required=True, label='Confirm',  widget=forms.TextInput(attrs={'type':'password'}))

    def clean(self):
        cleaned_data=super(SignUp, self).clean()
        p1=cleaned_data.get("password1")
        p2=cleaned_data.get("password2")
        if p1!= p2:
            raise forms.ValidationError("The passwords do not match")

    class Meta:
        model=User
        fields=('username','password1','password2')
