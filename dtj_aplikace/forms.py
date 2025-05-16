from django import forms
from .models import KontaktniZprava

class KontaktniFormular(forms.ModelForm):
    class Meta:
        model = KontaktniZprava
        fields = ['jmeno', 'email', 'zprava']
        labels = {
            'jmeno': '',
            'email': '',
            'zprava': '',
        }
        widgets = {
            'jmeno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jméno',
                'id': 'name-1'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'id': 'email-1'
            }),
            'zprava': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'zpráva',
                'rows': '6',
                'id': 'message-1'
            }),
        }