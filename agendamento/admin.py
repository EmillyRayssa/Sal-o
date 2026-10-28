from django.contrib import admin
from .models import Servico, Profissional, Cliente, Agendamento


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'duracao_minutos', 'ativo')


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'ativo')
    filter_horizontal = ('servicos',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')
    search_fields = ('nome', 'telefone')


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servico', 'profissional', 'data', 'hora', 'status')
    list_filter = ('status', 'data', 'profissional')
    search_fields = ('cliente__nome',)