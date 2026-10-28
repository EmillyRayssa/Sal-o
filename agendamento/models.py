from django.db import models


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_minutos = models.PositiveIntegerField(default=30)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"


class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    servicos = models.ManyToManyField(Servico, related_name='profissionais')
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Profissionais"

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    STATUS = [
        ('agendado', 'Agendado'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS, default='agendado')
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data', 'hora']
        constraints = [
            models.UniqueConstraint(
                fields=['profissional', 'data', 'hora'],
                name='horario_unico_por_profissional',
            )
        ]

    def __str__(self):
        return f"{self.cliente} - {self.servico} em {self.data} às {self.hora}"