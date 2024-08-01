from django import forms
from .models import Parto

class PartoForm(forms.ModelForm):
    class Meta:
        model = Parto
        fields = [
            'brinco', 'data_prov', 'data', 'ecc', 'tipo', 
            'sexo_cria1', 'peso_cria1', 
            'sexo_cria2', 'peso_cria2', 
            'sexo_cria3', 'peso_cria3', 
            'sexo_cria4', 'peso_cria4', 
            'manejo'
        ]
        widgets = {
            'data_prov': forms.DateInput(attrs={'type': 'date'}),
            'data': forms.DateInput(attrs={'type': 'date'}),
            'peso_cria1': forms.NumberInput(attrs={'step': '0.01'}),
            'peso_cria2': forms.NumberInput(attrs={'step': '0.01'}),
            'peso_cria3': forms.NumberInput(attrs={'step': '0.01'}),
            'peso_cria4': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sexo_cria2'].required = False
        self.fields['peso_cria2'].required = False
        self.fields['sexo_cria3'].required = False
        self.fields['peso_cria3'].required = False
        self.fields['sexo_cria4'].required = False
        self.fields['peso_cria4'].required = False
