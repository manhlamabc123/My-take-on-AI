from wsgiref import validate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator

class RegisterForm(UserCreationForm):
    email_regex = EmailValidator()
    email = forms.EmailField(validators=[email_regex])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=10)

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "password1", "password2"]