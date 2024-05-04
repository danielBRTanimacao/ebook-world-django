from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nome usuario...',
            }
        ),
        label="Nome de usuario"
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email...',
            }
        ),
        label="Digite um email valido"
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'passwordInput',
                'placeholder':'Sua senha...',
            }
        ),
        label="Digite uma senha"
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'passwordInput',
                'placeholder':'Confirme sua senha...',
            }
        ),
        label="Confirmar senha"
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe alguem com este email use outro', code='invalid')
            )
        return email

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nome...',
            }
        ),
        label="Nome de usuario"
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'passwordInput',
                'placeholder':'Confirme sua senha...',
            }
        ),
        label="Confirmar senha"
    )

    class Meta:
        model = User
        fields = (
            'username', 'password'
        )