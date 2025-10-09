from django import forms
from .models import Estabelecimento

class EstabelecimentoForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Estabelecimento
        fields = [
            'email', 'senha', 'razao_social', 'cnpj', 'nome_fantasia', 'inscricao_estadual',
            'endereco', 'numero', 'complemento', 'cidade', 'bairro', 'cep', 'telefone',
            'horario_inicio', 'horario_fim', 'logo', 'nome_proprietario', 'cargo_funcao',
            'rg', 'cpf', 'telefone_proprietario', 'responsavel_tecnico', 'formacao_academica',
            'conselho_classe', 'tipo_estabelecimento', 'tipo_manipulacao', 'num_funcionarios',
            'num_licenca_sanitaria'
        ]
