from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Evento(models.Model):
    nome_do_evento = models.CharField(max_length=250)
    data_do_evento = models.DateField()
    descricao_do_evento = models.TextField()
    local_do_evento = models.CharField(max_length=250)

    def __str__(self):
        return self.nome_do_evento


class Participante(models.Model):
    nome_do_participante = models.CharField(max_length=250)
    email = models.EmailField()
    numero_telefone = models.CharField(max_length=20)
    informacoes_adicionais = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_do_participante


class Ingresso(models.Model):
    tipo_de_ingresso = models.CharField(max_length=200)
    preco_do_ingresso = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_de_ingressos = models.PositiveIntegerField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_de_ingresso


class Participacao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    hora_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.evento} - {self.participante}"


class Palestrante(models.Model):
    nome_do_palestrante = models.CharField(max_length=250)
    resumo_do_palestrante = models.TextField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_do_palestrante


class Palestra(models.Model):
    titulo_da_palestra = models.CharField(max_length=250)
    descricao_da_palestra = models.TextField()
    palestrante = models.ForeignKey(Palestrante, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo_da_palestra


class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    palestra = models.ForeignKey(Palestra, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participante} - {self.palestra}"