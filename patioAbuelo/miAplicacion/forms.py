from django import forms
from .models import Mozo

class MozoForm(forms.ModelForm):
    class Meta:
        model = Mozo
        fields = ('nombre', 'telefono')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }