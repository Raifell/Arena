from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreateUserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('photo', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UpdateUserForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('photo', 'username', 'first_name', 'last_name', 'email')

