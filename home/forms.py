from django import forms
from django.core.exceptions import ValidationError

from home.models import Home

class HomeForm(forms.ModelForm):
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
        )

    def clean(self):
        self.add_error(
            'username',
            ValidationError(
                'Mensagem de Erro teste 1',
                code='invalid'
            )
        )
        return super().clean()