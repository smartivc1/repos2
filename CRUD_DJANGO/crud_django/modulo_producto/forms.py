from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["user", "nombreProducto", "stockActual", "stockInicial",
                  "estado", "precio"]
        widgets = {'nombreProducto': forms.TextInput(attrs={'class':'form-control',
                                                           'placeholder':'Titulo'}),
                   'stockActual': forms.NumberInput(attrs={'class':'form-control',
                                                          'placeholder':'Titulo'}),
                   'stockInicial': forms.NumberInput(attrs={'class':'form-control',
                                                           'placeholder':'Titulo'}),
                   'precio': forms.NumberInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Titulo'}),
                   }
        labels = {'title':'','order':'','content':''}