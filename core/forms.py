from django.forms import ModelForm
from .models import Pessoa


# Formulário da classe person
class PersonForm(ModelForm):
    class Meta:
        model = Pessoa
        # Dados que serão preenchidos no formulario, nesse caso, todos
        fields = '__all__'