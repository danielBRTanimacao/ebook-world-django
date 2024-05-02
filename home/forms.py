from django import forms
from django.core.exceptions import ValidationError

from home.models import Home

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
        model = Home
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

