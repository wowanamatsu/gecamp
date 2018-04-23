from django import forms

from .models import Pessoa


class FormPessoa(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Adiciona uma class CSS aos campos do formulário.
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        # Altera a class CSS de um campo específico.
        self.fields['nome_social'].widget.attrs.update({'class':'form-control'})


    class Meta:
        model = Pessoa
        fields = ['nome', 'nome_social', 'endereco', 'sexo', 'data_nascimento']
        widgets = {}
