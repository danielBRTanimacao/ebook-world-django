from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HomeForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        ),
        label='Foto perfil'
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nome usuario...',
            }
        ),
        label="Digite seu nome de usuario"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':'passwordInput',
                'placeholder':'Sua senha...',
            }
        ),
        help_text='Digite uma senha com 8 ou mais caracteres',
        label="Digite uma senha"
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

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'picture',
        )

    def clean(self):
        username = self.cleaned_data.get('username')
        try:
            int(username)
            self.add_error(
                'username',
                ValidationError(
                    'Seu nome não pode conter apenas números!'
                )
            )
        except ValueError:
            ...
        
        return super().clean()
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            self.add_error(
                'password',
                ValidationError(
                    'Digite uma senha igual ou com mais de 8 caracteres!'
                )
            )
        return password

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

