from django import forms
from .models import Agendamento


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'servico', 'profissional', 'data', 'hora', 'observacoes']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        dados = super().clean()
        profissional = dados.get('profissional')
        servico = dados.get('servico')
        data = dados.get('data')
        hora = dados.get('hora')

        if profissional and servico and servico not in profissional.servicos.all():
            raise forms.ValidationError("Esse profissional não realiza o serviço escolhido.")

        if profissional and data and hora:
            existe = Agendamento.objects.filter(
                profissional=profissional, data=data, hora=hora
            ).exclude(status='cancelado').exists()
            if existe:
                raise forms.ValidationError("Esse horário já está ocupado para o profissional.")
        return dados