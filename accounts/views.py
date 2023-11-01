# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .froms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            username = form.cleaned_data('username')
            password = form.cleaned_data('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, 'registration/signup.html', context)
