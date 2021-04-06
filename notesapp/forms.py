from django import forms
from django.contrib.auth.models import User
from notesapp import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class UserCreateForm(UserCreationForm):
    class Meta:
        fields =('first_name','last_name','username','email','password1','password2')
        model = User
