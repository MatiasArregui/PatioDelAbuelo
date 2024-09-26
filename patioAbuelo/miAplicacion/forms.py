from django import forms
from .models import Mozo, Cliente, Carta, Categoria, SubCategoria

class MozoForm(forms.ModelForm):
    class Meta:
        model = Mozo
        fields = ('nombre', 'telefono')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("nombre", "telefono", "direccion")
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            
        }

class CartaForm(forms.ModelForm):
    class Meta:
        model = Carta
        fields = ("nombre", "precio", "controlStock", "stock", "categoria", "subCategoria")
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "controlstock" : forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input form-control'})),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control", "onchange":"updateSelect2()"}),
            "subCategoria":forms.Select(attrs={"class": "form-control"}),
        }
    #     #Hacer filtrado por js
    # def __init__(self, *args, **kwargs):
    #     super(CartaForm, self).__init__(*args, **kwargs)
    #     # Acceder al valor de un campo anterior
    #     if 'categoria' in self.data:
    #         categoria_id = int(self.data.get('categoria'))
    #         # print(categoria_id)
    #         # Filtrar el queryset del campo 'precio' basado en el valor de 'categoria'
    #         self.fields['subCategoria'].queryset = SubCategoria.objects.filter(id_categoria=categoria_id)