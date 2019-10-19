from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def clean_email(self):
        data = self.cleaned_data['email']
        return data.lower()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class UpdateCustomUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        user = get_user_model().objects.exclude(pk=self.instance.pk).filter(username__iexact=username).first()
        if user == None:
            return username
        else:
            raise forms.ValidationError(f'Username "{username}" is already in use.')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = get_user_model().objects.exclude(pk=self.instance.pk).get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError(f'Username "{email}" is already in use.')
