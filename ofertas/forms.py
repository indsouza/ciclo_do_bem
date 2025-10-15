from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ["nome_produto", "descricao", "foto", "data_validade_produto", "data_expiracao_oferta", "quantidade"]
        widgets = {
            "data_validade_produto": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "DD/MM/AAAA"
            }),
            "data_expiracao_oferta": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control",
                "placeholder": "DD/MM/AAAA HH:MM"
            }),
        }
