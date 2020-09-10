from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import requests
import json
from .forms import PersonForm
from .models import Pessoa


# So pode ser acessado com login
@login_required
def personList(request):
    termo_busca = request.GET.get('pesquisa', None)

    # Filtro para a pesquisa
    if termo_busca:
        pessoas = Pessoa.objects.filter(nome__icontains=termo_busca)
    else:
        pessoas = Pessoa.objects.all()

    return render(request, 'core/person_list.html', {'pessoas': pessoas})

# So pode ser acessado com login
@login_required
def newPerson(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    api = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio')
    r = json.loads(api.text)
    nome = r[0]
    sobrenome = r[1] + ' ' + r[2]
    form.initial['nome'] = nome
    form.initial['sobrenome'] = sobrenome
    if form.is_valid():
        pessoa = form.save(commit=False)
        form.save()
        # Quando salvar, retorna para a lista de pessoas
        return redirect('personList')
    return render(request, 'core/person_form.html', {'form': form})

# So pode ser acessado com login
@login_required
def personUpdate(request, id):
    # Variavel que recebe o id da pessoa
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'core/person_form.html', {'form': form})

# So pode ser acessado com login
@login_required
def personDelete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('personList')

    return render(request, 'core/person_delete_confirm.html', {'pessoa': pessoa})
