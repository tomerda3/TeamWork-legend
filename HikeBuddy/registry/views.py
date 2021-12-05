from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib.auth.models import Group

# Create your views here.
def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            Group.objects.get_or_create(name=form.cleaned_data['userType'])
            cur_group = Group.objects.get(name=form.cleaned_data['userType'])
            cur_group.user_set.add(user)
            print(form.cleaned_data['phone'])  # Not yet really saved
            return redirect("/login/")
    else:
        form = RegisterForm()
    return render(response, "registry/signup.html", {"form":form})