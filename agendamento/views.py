from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Agendamento
from .forms import AgendamentoForm


def lista_agendamentos(request):
    agendamentos = Agendamento.objects.select_related('cliente', 'servico', 'profissional')
    return render(request, 'agendamento/lista.html', {'agendamentos': agendamentos})


def novo_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Agendamento realizado com sucesso!")
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento/form.html', {'form': form})