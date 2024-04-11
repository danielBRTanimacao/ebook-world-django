from django import forms
from django.core.exceptions import ValidationError

from home.models import Home

class HomeForm(forms.ModelForm):
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