from django import forms

class PerguntaForm(forms.Form):
	titulo = forms.CharField(max_length=200)
	pergunta = forms.CharField(widget=forms.Textarea)

class ComentarioForm(forms.Form):
	comentario = forms.CharField(widget=forms.Textarea)
