from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class SignupForm(UserCreationForm):
    name = forms.CharField(label= 'Name', required=True, widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'})) 
    email = forms.EmailField(label= 'Email', required=True, widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password1 = forms.CharField(label= 'Password',widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
    password2 = forms.CharField(label= 'Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = UsernameField(label=_('Email'),widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class ChangepasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))  
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control'}),help_text=password_validation.password_validators_help_text_html())    
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control'}))    

class ResetpasswordForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'), required=True, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))

class PasswordsetForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'), required=True, strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())    
    new_password2 = forms.CharField(label=_('Confirm New Password'), required=True, strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control'}))    