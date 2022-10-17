from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': 'required' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': 'required' }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': 'required' }),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': 'required' }),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required' }),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('confirm_password', 'phone_number', 'address')

        labels = {
            'confirm_password': '',
            'phone_number': '',
            'address': '',
        }

        widgets = {
            'confirm_password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'required': 'required'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        }
