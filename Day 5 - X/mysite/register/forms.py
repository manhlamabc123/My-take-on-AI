from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from main.models import Member


class UserForm(UserCreationForm):
    email_regex = EmailValidator()
    email = forms.EmailField(validators=[email_regex])

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class DateInput(forms.DateInput):
    input_type = 'date'

class MemberForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex])

    class Meta:
        model = Member
        fields = ['birthday', 'phone_number']
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
        }