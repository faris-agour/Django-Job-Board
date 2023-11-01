# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .froms import SignupForm
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            username = form.cleaned_data('username')
            password = form.cleaned_data('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile/profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {"form": form})


def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'profile/profile.html', {'profile': profile})


def profile_edit(request):
    pass
