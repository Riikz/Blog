from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm, EditUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('blog:index')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:index')


@login_required(login_url="/accounts/login")
def profile_view(request):
    user = request.user
    following = list(user.userprofile.follow.all())
    followers = list(user.userprofile.followers.all())
    args = {
        'user': user,
        'follow_list': following,
        'followers': followers,
    }
    return render(request, 'accounts/profile.html', args)


@login_required(login_url="/accounts/login")
def edit_view(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        form1 = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('accounts:profile')
    else:
        form = EditUserForm(instance=request.user)
        form1 = UpdateProfileForm(instance=request.user.userprofile)
    args = {
        'form': form,
        'form1': form1,
            }
    return render(request, 'accounts/edit_profile.html', args)


@login_required(login_url="/accounts/login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')

    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'accounts/change-password.html', args)


@login_required(login_url="/accounts/login")
def follow_view(request, pk):
    follower = request.user
    to_be_followed = User.objects.get(pk=pk)
    if follower == to_be_followed:
        return redirect('blog:index')
    follower.userprofile.follow.add(to_be_followed)
    to_be_followed.userprofile.followers.add(follower)
    follower.save()
    return redirect('blog:index')


@login_required(login_url="/accounts/login")
def unfollow_view(request, pk):
    follower = request.user
    unfollowing = User.objects.get(pk=pk)
    follower.userprofile.follow.remove(unfollowing)
    unfollowing.userprofile.followers.remove(follower)
    unfollowing.userprofile.subscribe.remove(follower)
    return redirect('blog:index')


@login_required(login_url='/accounts/login')
def subscribe_email(request, pk):
    follower = request.user
    to_be_followed = User.objects.get(pk=pk)
    if follower == to_be_followed:
        return redirect('blog:index')
    follower.userprofile.follow.add(to_be_followed)
    to_be_followed.userprofile.followers.add(follower)
    to_be_followed.userprofile.subscribe.add(follower)
    return redirect('blog:index')


@login_required(login_url="/accounts/login")
def unsubscribe_email(request, pk):
    follower = request.user
    unfollowing = User.objects.get(pk=pk)
    unfollowing.userprofile.subscribe.remove(follower)
    return redirect('blog:index')
