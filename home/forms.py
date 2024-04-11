from django import forms

from home.models import Home

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = (
            'username',
            'email',
            'password',
        )
