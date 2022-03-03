from django.shortcuts import redirect, render
from .forms import UserForm, MemberForm
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == 'POST':
        user_form = UserForm(response.POST)
        member_form = MemberForm(response.POST)
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            member_form = member_form.save(commit=False)
            member_form.user = user
            member_form.save()
            messages.success(response, f'Registration complete! You may log in!')
        
        return redirect("/login")
    else:
        user_form = UserForm()
        member_form = MemberForm()

    return render(response, "register/register.html", {"user_form": user_form, "member_form": member_form})