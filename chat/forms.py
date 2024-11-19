from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'register-form', 'placeholder': 'Username', }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'register-form', 'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'register-form', 'placeholder': 'Password'}) , label = "Password")
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'register-form2', 'placeholder': 'Password Again'}), label = "Password Again")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user