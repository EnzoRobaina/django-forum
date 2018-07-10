from django import forms
from .models import *
from django.utils import timezone
from django.forms import ModelForm, Textarea, TextInput
from ckeditor.widgets import CKEditorWidget



class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = '__all__'
        exclude = ['data_postagem']
        widgets = {
            'texto': CKEditorWidget()
        }
        


class RespostaForm(ModelForm):
    class Meta:
        model = Resposta
        fields = '__all__'
        exclude = ['data_postagem']
        widgets = {
            'texto': CKEditorWidget()
        }

class DiscussaoForm(ModelForm):
    class Meta:
        model = Discussao
        exclude = ['__all__']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'password', 'first_name', 'last_name', 'email']

