from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    studentnum = forms.CharField(max_length=9)

    class Meta:
        model = User
        fields = ('username', 'studentnum', 'password1', 'password2')