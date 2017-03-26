from django.shortcuts import render
from .models import Pergunta
from django.utils import timezone

# Create your views here.
def pergunta(request):
	perguntas = Pergunta.objects.filter(data_de_criacao__lte=timezone.now()).order_by('data_de_criacao')
	return render(request, 'guru_responde/pergunta.html', {'perguntas' : perguntas})

def detalhe(request, pergunta_id):
	pergunta = Pergunta.objects.get(id=pergunta_id)
	return render(request, 'guru_responde/detalhe.html', {'pergunta' : pergunta})