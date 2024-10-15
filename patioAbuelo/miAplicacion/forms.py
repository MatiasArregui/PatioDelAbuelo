from django import forms
from .models import Mozo, Cliente, Carta, Categoria, SubCategoria, CartaOrden, Orden, Factura, FacturaOrden
from django.forms import inlineformset_factory
class MozoForm(forms.ModelForm):
    class Meta:
        model = Mozo
        fields = ('nombre', 'telefono')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {"nombre":"Nombre",
                  "telefono":"Teléfono"
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
        labels= {
            "nombre": "Nombre",
            "telefono": "Teléfono",
            "direccion": "Dirección",
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
            "categoria": forms.Select(attrs={"class": "form-control", "onchange":"updateSelect2()","disabled":"true"}),
            "subCategoria":forms.Select(attrs={"class": "form-control", "disabled":"true"}),
        }
        labels = {
            "nombre": "Nombre",
            "precio": "Precio",
            "controlStock": "Verificar stock",
            "stock": "Stock",
            "categoria": "Categoría",
            "subCategoria": "Subcategoría",
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
    
class CartaOrdenForm(forms.ModelForm):
    class Meta:
        model = CartaOrden
        fields = ("id_carta", "cantidad")
        widgets = {
            "id_carta": forms.Select(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels ={
            "id_carta": "Plato",
        }

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ("total", "observacion", "id_mesa", "id_mozo", "entregado")
        widgets = {
            "total": forms.NumberInput(attrs={"class": "form-control"}),
            "observacion": forms.Textarea(attrs={"class": "form-control"}),
            "id_mesa" : forms.Select(attrs={'class':'form-control'}),
            "id_mozo": forms.Select(attrs={"class": "form-control"}),
            "entregado": forms.CheckboxInput(attrs={'class': 'form-check-input form-control'}),
        }
        labels = {
            "id_mesa": "Mesa",
            "id_mozo": "Mozo",
        }

CartaOrdenFormSet = inlineformset_factory(Orden, CartaOrden, form=CartaOrdenForm, extra=3)

class FacturaOrdenForm(forms.ModelForm):
    class Meta:
        model = FacturaOrden
        fields = ("id_orden",)
        widgets = {
            "id_orden": forms.Select(attrs={"class": "form-control"}),
        }
        labels ={
            "id_orden": "Orden",
        }
        

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ("total", "id_cliente")
        widgets = {
            "total": forms.NumberInput(attrs={"class": "form-control"}),
            "id_cliente" : forms.Select(attrs={'class':'form-control'}),
        }
        labels ={
            "total": "Total",
            "id_cliente": "Cliente"
        }

FacturaOrdenFormSet = inlineformset_factory(Factura, FacturaOrden, form=FacturaOrdenForm, extra=3)