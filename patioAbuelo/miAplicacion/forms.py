from django import forms
from .models import Mozo, Cliente, Carta, Categoria, SubCategoria, CartaOrden, Orden, Factura, FacturaOrden, FacturaPago, Cierre, FacturaCierre, PlatoDia
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm

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
        fields = ("nombre", "precio", "controlStock", "stock", "categoria", "subCategoria", "imagen", "descripcion")
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "controlstock" : forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input form-control'})),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control", "onchange":"updateSelect2()"}),
            "subCategoria":forms.Select(attrs={"class": "form-control", "disabled":"true"}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        labels = {
            "nombre": "Nombre",
            "descripcion":"Descripción",
            "precio": "Precio",
            "controlStock": "Verificar stock",
            "stock": "Stock",
            "categoria": "Categoría",
            "subCategoria": "Subcategoría",
            "imagen":"Imagen del Producto",
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
            "id_carta": forms.Select(attrs={"class": "form-control carta"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control cant"}),
        }


class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ("observacion", "id_mesa", "id_mozo", "total", "entregado")
        widgets = {
            "observacion": forms.Textarea(attrs={"class": "form-control"}),
            "id_mesa" : forms.Select(attrs={'class':'form-control'}),
            "id_mozo": forms.Select(attrs={"class": "form-control"}),
            "total": forms.NumberInput(attrs={"class": "form-control bg-danger text-white", "readonly":True}),
            "entregado": forms.CheckboxInput(attrs={'class': 'form-check-input form-control'}),
        }
        labels = {
            "id_mesa": "Mesa",
            "id_mozo": "Mozo",
        }

CartaOrdenFormSet = inlineformset_factory(Orden, CartaOrden, form=CartaOrdenForm, extra=6)

class FacturaPagoForm(forms.ModelForm):
    class Meta:
        model = FacturaPago
        fields = ("id_tipoPago", "total")
        widgets = {
            "id_tipoPago": forms.Select(attrs={"class": "form-control"}),
            "total": forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels ={
            "id_tipoPago": "Tipo Pago",
        }
        
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
        fields = ("id_cliente", "total", "total_pago", "vuelto")
        widgets = {
            "id_cliente" : forms.Select(attrs={'class':'form-control'}),
            "total": forms.NumberInput(attrs={"class": "form-control","readonly":True}),
            "total_pago": forms.NumberInput(attrs={"class": "form-control","readonly":True}),
            "vuelto": forms.NumberInput(attrs={"class": "form-control","readonly":True}),
        }
        labels ={
            "total": "Total",
            "id_cliente": "Cliente"
        }

FacturaOrdenFormSet = inlineformset_factory(Factura, FacturaOrden, form=FacturaOrdenForm, extra=3)
FacturaPagoFormSet = inlineformset_factory(Factura, FacturaPago, form=FacturaPagoForm, extra=3)

class FacturaCierreForm(forms.ModelForm):
    class Meta:
        model = FacturaCierre
        fields = ("id_factura",)
        widgets = {
            "id_factura": forms.Select(attrs={"class": "form-control"}),
        }
        labels ={
            "id_factura": "Factura",
        }

class CierreForm(forms.ModelForm):
    class Meta:
        model = Cierre
        fields = ('total_ordenes', "total_facturas", 'vuelto')
        widgets = {
            'total_ordenes': forms.NumberInput(attrs={'class': 'form-control', "readonly":True}),
            'total_facturas': forms.NumberInput(attrs={'class': 'form-control', "readonly":True}),
            'vuelto': forms.NumberInput(attrs={'class': 'form-control', "readonly":True}),
        }
        labels = {"total_ordenes":"Total Ordenes",
                  "total_facturas":"Total Facturas",
                  "vuelto":"Vuelto",
            }
FacturaCierreFormSet = inlineformset_factory(Cierre, FacturaCierre, form=FacturaCierreForm, extra=3)

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )


class PlatoDiaForm(forms.ModelForm):
    class Meta:
        model = PlatoDia
        fields = ['id_carta']
        widgets = {
            'id_carta': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {"id_carta":"Plato del día"
            }

        