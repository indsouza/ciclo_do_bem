from django import forms
from .models import Instituicao

class InstituicaoForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(), label="Senha")

    class Meta:
        model = Instituicao
        fields = [
            'email', 'senha', 'razao_social', 'cnpj', 'nome_fantasia', 'inscricao_estadual',
            'endereco', 'numero', 'complemento', 'cidade', 'bairro', 'cep', 'telefone',
            'horario_inicio', 'horario_fim', 'logo', 'nome_responsavel', 'cargo_funcao',
            'rg', 'cpf', 'telefone_responsavel', 'responsavel_tecnico', 'formacao_academica',
            'conselho_classe'
        ]

    def save(self, commit=True):
        usuario = super().save(commit=False)
        # agora salva a senha em texto simples (sem set_password)
        usuario.senha = self.cleaned_data['senha']
        if commit:
            usuario.save()
        return usuario
