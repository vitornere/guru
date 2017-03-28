from django.shortcuts import render
from .models import Pergunta
from django.utils import timezone
from .forms import PerguntaForm, ComentarioForm
from django.contrib.auth.models import User

# Create your views here.
def pergunta(request):
	perguntas = Pergunta.objects.filter(data_de_criacao__lte=timezone.now()).order_by('data_de_criacao')
	return render(request, 'guru_responde/pergunta.html', {'perguntas' : perguntas})

def detalhe(request, pergunta_id):
	pergunta = Pergunta.objects.get(id=pergunta_id)
	if request.method == "POST":
		form = ComentarioForm(request.POST)
		if form.is_valid():
			texto = form.cleaned_data['comentario'];
			autor = User.objects.get(id=1)
			data_de_criacao = timezone.now()
			comentario = pergunta.resposta_set.create(autor=autor, texto=texto, data_de_criacao=data_de_criacao)
			comentario.save()
			form = ComentarioForm()
			return render(request, 'guru_responde/detalhe.html', {'pergunta' : pergunta, 'form' : form})
		else:
			return render(request, 'guru_responde/detalhe.html', {'pergunta' : pergunta, 'form' : form})
	else:
		form = ComentarioForm()
		pergunta = Pergunta.objects.get(id=pergunta_id)
		return render(request, 'guru_responde/detalhe.html', {'pergunta' : pergunta, 'form' : form})

def nova_pergunta(request):
	if request.method == "POST":
		form = PerguntaForm(request.POST)
		if form.is_valid():
			titulo = form.cleaned_data['titulo']
			texto = form.cleaned_data['pergunta']
			autor = User.objects.get(id=1)
			data_de_criacao = timezone.now()
			pergunta = Pergunta.objects.create(autor=autor, titulo=titulo, texto=texto, data_de_criacao=data_de_criacao, data_de_fechamento=None)
			pergunta.save()
			form = ComentarioForm()
			return render(request, 'guru_responde/detalhe.html', {'pergunta' : pergunta, 'form' : form})
		else:
			return render(request, 'guru_responde/nova_pergunta.html', {'form' : form})
	else:
		form = PerguntaForm()
		return render(request, 'guru_responde/nova_pergunta.html', {'form' : form})