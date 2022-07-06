from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from blog.models import Post
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

from .forms import Userupdate , profileUpdate

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def logout_views(request):
    logout(request)
    messages.success(request, f'You have been logged out')
    return redirect('blog-home')


@login_required
def profile(request):
    posts = Post.objects.filter(author = request.user)

    return render(request , 'users/profile.html', {'posts':posts})

@login_required
def updateprofile(request):
    if request.method == 'POST':
        user_form = Userupdate(request.POST, instance=request.user)
        profile_update = profileUpdate(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_update.is_valid():
            user_form.save()
            profile_update.save()
    else:
        user_form = Userupdate(instance=request.user)
        profile_update = profileUpdate(instance=request.user)
    return render(request, 'users/update_profile.html', {'user_form': user_form, 'profile_form': profile_update})