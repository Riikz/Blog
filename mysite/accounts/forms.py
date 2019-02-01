from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
        ]


class EditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['profile_image']

