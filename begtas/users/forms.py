from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django import forms
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите почту',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
    }))

    class Meta:
        model = User
        field = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите фамилию'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))

    # email = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Введите почту'
    # }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердить пароль'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(), required=False)

    last_name = forms.CharField(widget=forms.TextInput(), required=False)

    image = forms.ImageField(widget=forms.FileInput(), required=False)

    bio = forms.CharField(widget=forms.TextInput(), required=False)

    username = forms.CharField(widget=forms.TextInput(), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'bio', 'username')

