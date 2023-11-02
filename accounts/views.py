# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

from .froms import SignupForm, UserForm, ProfileForm
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
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=request.user.profile)
    context = {'userform': userform, 'profileform': profileform}
    return render(request, 'profile/profile_edit.html', context)
