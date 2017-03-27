from django import forms

class NameForm(forms.Form):
    nova_pergunta = forms.Textarea()