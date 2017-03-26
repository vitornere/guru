from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	data_de_criacao = models.DateTimeField(default=timezone.now)
	data_de_fechamento = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.titulo

	def fechar_duvida(self):
		self.data_de_fechamento = timezone.now()
		self.save()

class Resposta(models.Model):
	pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
	autor = models.ForeignKey('auth.User')
	texto = models.TextField()
	data_de_criacao = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.texto