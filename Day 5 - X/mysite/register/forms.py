from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from main.models import User

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'user-form'
        self.helper.attrs = {
            "hx-post": reverse_lazy("register"),
            "hx-target": "#user-form",
            "hx-swap": "outerHTML"
        }
        self.helper.add_input(Submit('submit', 'Register'))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "birthday", "phone_number", "email", "password"]
        widgets = {
            "password": forms.PasswordInput(),
            # "username": forms.TextInput(
            #     attrs={
            #         "hx-get": reverse_lazy("register"),
            #         "hx-trigger": "keyup"
            #     }
            # ),
            "birthday": forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
        }

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) <= 3:
            raise forms.ValidationError("Username is too short")
        return username

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user