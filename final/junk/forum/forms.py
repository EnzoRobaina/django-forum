from django import forms
from .models import *
from django.utils import timezone
from django.forms import ModelForm, Textarea, TextInput


class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = '__all__'
        exclude = ['data_postagem']
        widgets = {
            'autor': TextInput(attrs={'class':'form-control'}),
            'titulo': TextInput(attrs={'class':'form-control'}),
            'texto': Textarea(attrs={'class': 'form-control'})
        }
    
class RespostaForm(ModelForm):
    class Meta:
        model = Resposta
        fields = '__all__'
        exclude = ['data_postagem']
        widgets = {
            'autor': TextInput(attrs={'class':'form-control'}), 
            'texto': Textarea(attrs={'class': 'form-control'})
        }

class ForumForm(ModelForm):
    class Meta:
        model = Forum
        exclude = ['__all__']