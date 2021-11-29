from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    USER_TYPES = [('traveler', 'Traveler'),
    ('guide', 'Guide'),
    ('host', 'Host'),]
    userType = forms.CharField(label='User type', widget=forms.Select(choices=USER_TYPES))
    
    class Meta:
        model = User
        fields = ["username", "userType", "email", "password1", "password2"]