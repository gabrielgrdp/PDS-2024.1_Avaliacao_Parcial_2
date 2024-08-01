from django.shortcuts import render, redirect
from .models import Parto
from .forms import PartoForm

def lista_partos(request):
    partos = Parto.objects.all()
    return render(request, 'partos/lista_partos.html', {'partos': partos})

def novo_parto(request):
    if request.method == 'POST':
        form = PartoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_partos')
    else:
        form = PartoForm()
    return render(request, 'partos/novo_parto.html', {'form': form})
