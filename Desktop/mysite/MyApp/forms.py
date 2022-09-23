from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import MaxLengthValidator, MinLengthValidator

from MyApp.models import CustomUser


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Password', 'required': 'True'}), required=False)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Confirm your Password', 'required': 'True'}), required=False)
    contact_information = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter your phone no.', 'required': 'True'}),
        validators=[MaxLengthValidator(11), MinLengthValidator(11)], required=False)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter your first name', 'required': 'True'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter your last name', 'required': 'True'}), required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'contact_information', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control form-control-user', "placeholder": "Email", 'required': 'True'}),
        }


class EditProfileForm(UserChangeForm):
    contact_information = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}),
        validators=[MaxLengthValidator(11), MinLengthValidator(11)])
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'contact_information', 'address', 'date_of_birth']
