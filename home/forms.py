from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

from .models import Post

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

class RegisterUpdateForm(forms.ModelForm):

    username = forms.CharField(
        min_length=5,
        max_length=30,
        label='Seu nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome...'
            }
        ),
        help_text='Crie um nome novo valido',
        required=False,
    )

    email = forms.EmailField(
        label='Novo Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Email...',
            }
        ),
        help_text='Crie um email valido',
        required=False,
    )


    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control',
                'id': 'passwordShow'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label='Segunda Senha',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control',
                'id': 'passwordShow'
            }
        ),
        help_text='Use a mesma senha anterior',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')
        
        if password:
            user.set_password(password)

        if commit:
            user.save()
        
        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem!')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error('email',ValidationError('Já existe esse email use outro', code='invalid'))

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))
        
        return password1
    
class FormForPost(forms.ModelForm):

    post_picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }
        ),
        label="imagem para post",
        required=True
    )

    simple_text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        ),
        label="Descrição",
        required=True
    )

    class Meta:
        model = Post
        fields = (
            'post_picture', 'simple_text'
        )