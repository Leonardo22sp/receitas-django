# receitas/views.py

from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
    categoria_selecionada = request.GET.get('categoria')
    if categoria_selecionada:
        receitas = Receita.objects.filter(categoria=categoria_selecionada) # <-- ALTERADO
    else:
        receitas = Receita.objects.all()
    
    return render(request, 'receitas/home.html', {'receitas': receitas})

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})

def pesquisar_receitas(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Receita.objects.filter(title__icontains=query)
    return render(request, 'receitas/pesquisar_receitas.html', {
        'query': query,
        'receitas': resultados
    })

def sobre_nos(request):
    return render(request, 'receitas/sobre_nos.html')

def contato(request):
    from .forms import ContatoForm
    sucesso = False
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
    else:
        form = ContatoForm()
    return render(request, 'receitas/contato.html', {'form': form, 'sucesso': sucesso})