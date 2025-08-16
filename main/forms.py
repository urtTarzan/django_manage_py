from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Post
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","description"]