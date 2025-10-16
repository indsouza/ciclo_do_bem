from django import forms
from .models import Estabelecimento

# Opções pré-definidas
TIPO_ESTABELECIMENTO_CHOICES = [
    ('padaria', 'Padaria'),
    ('restaurante', 'Restaurante'),
    ('supermercado', 'Supermercado'),
    ('farmacia', 'Farmácia'),
    ('outro', 'Outro'),
]

TIPO_MANIPULACAO_CHOICES = [
    ('preparo', 'Preparo'),
    ('revenda', 'Revenda'),
]

class EstabelecimentoForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Senha",
        required=True
    )
    confirm_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirmar Senha",
        required=True
    )

    tipo_estabelecimento = forms.ChoiceField(
        choices=TIPO_ESTABELECIMENTO_CHOICES,
        label="Tipo de Estabelecimento",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    tipo_manipulacao = forms.ChoiceField(
        choices=TIPO_MANIPULACAO_CHOICES,
        label="Tipo de Manipulação",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Estabelecimento
        fields = [
            'email', 'razao_social', 'cnpj', 'nome_fantasia', 'inscricao_estadual',
            'endereco', 'numero', 'complemento', 'cidade', 'bairro', 'cep', 'telefone',
            'horario_inicio', 'horario_fim', 'logo', 'nome_proprietario', 'cargo_funcao',
            'rg', 'cpf', 'telefone_proprietario', 'responsavel_tecnico', 'formacao_academica',
            'conselho_classe', 'num_funcionarios', 'num_licenca_sanitaria'
        ]

    def clean(self):
        """Valida se senha e confirm_senha coincidem"""
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirm_senha = cleaned_data.get("confirm_senha")
        if senha != confirm_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        """Salva o usuário com senha criptografada"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['senha'])
        # Salva os campos de escolha
        user.tipo_estabelecimento = self.cleaned_data['tipo_estabelecimento']
        user.tipo_manipulacao = self.cleaned_data['tipo_manipulacao']
        if commit:
            user.save()
        return user
