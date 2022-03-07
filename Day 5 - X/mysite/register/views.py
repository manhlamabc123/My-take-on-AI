from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form

# Create your views here.
def register(response):
    if response.method == 'POST':
        user_form = UserForm(response.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("/login")

        ctx = {}
        ctx.update(csrf(response))
        form_html = render_crispy_form(user_form, context = ctx)
        return HttpResponse(form_html)
    else:
        user_form = UserForm()

    return render(response, "register/register.html", {"user_form": user_form})