from django import forms

from .models import Pais

class FormPais(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		# Adiciona uma class CSS aos campos do formulário.
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Pais
		fields = '__all__'