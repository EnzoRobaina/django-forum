from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import Http404
from django.utils import timezone
from django.db.models import Count

from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib import messages
from django.db.models import Q


def log(request):
    #next_url = ""
    next_url = request.GET.get("next")
    #if request.GET:  
    #    next_url = request.GET['next']
    #next_url = request.GET.get("next")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('forum')
            else:
                messages.error(request, "Usuário inativo!")
        else:
            messages.error(request, "Usuário ou senha inválidos!")

    context = {}
    return render(request, 'forum/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def registrar(request):
    
    #import ipdb; ipdb.set_trace()
   
    form = UserForm(request.POST, request.FILES or None)
    #verifica se o usuario já existe
    if User.objects.filter(username=request.POST.get('username')).exists():
        messages.error(request, "Nome de usuário em uso, escolha outro!")
    #verifica se o email já foi usado
    if request.POST.get('email') != "":
        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request, "Este email já está associado à uma conta.")
    #verifica se os campos foram preenchidos corretamente
    if form.is_valid():   
        user = form.save(commit=False)
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.avatar = form.cleaned_data['avatar']
        user.set_password(password)
        
        

        user.save()
        
        
        
        #autentica o usuário recém registrado
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('forum')
            else:
                messages.error(request, "Usuário inativo!")
        else:
                messages.error(request, "Usuário inválido!")
    else:  
        if request.method == 'POST':
            messages.error(request, "Preencha os campos corretamente!")
    context = {'form':form}            
    return render(request, 'forum/registrar.html', context)






    # RespostaForm(request.POST or None)

    # def get(self, request):
    #     form = self.form_class(None)
    #     context = {'form':form, 'mensagem':self.mensagem}
    #     return render(request, 'forum/registrar.html', context)
    
    # def post(self, request):
        
    #     form = self.form_class(request.POST)
    #     self.mensagem = "NAO EXISTE"
        

def forum(request):
    discussao_lista = Discussao.objects.all()
    quantidades = {}
    #contando os topicos para cada discussao e armazenando em um dicionario
    for d in discussao_lista:
        quantidades.update({d.titulo:Topico.objects.filter(discussao_fk__titulo=d.titulo).count()})
    #import ipdb; ipdb.set_trace()
    context = {'discussao_lista': discussao_lista, 'quantidades':quantidades}
    return render(request, 'forum/forum.html', context)

def discussao(request, discussao_titulo):
    quantidade_respostas = {}
    topicos = Topico.objects.all()
    #contando as respostas para cada topico e armazenando em um dicionario
    for t in topicos:
        quantidade_respostas.update({t.titulo:Resposta.objects.filter(topico_fk__titulo=t.titulo).count()})

    pesquisa = request.GET.get("pesquisa")
    if pesquisa:
        topicos_lista = Topico.objects.filter(Q(titulo__icontains=pesquisa) | Q(texto__icontains=pesquisa), Q(discussao_fk__titulo = discussao_titulo))
        
    else:
        try:
            Discussao.objects.get(titulo=discussao_titulo)
        except Discussao.DoesNotExist:
            raise Http404("Discussão não existe")
        
        topicos_lista = Topico.objects.filter(discussao_fk__titulo = discussao_titulo).order_by('-data_postagem')
    context = {'topicos_lista':topicos_lista, 'quantidade_respostas':quantidade_respostas}
    return render(request, 'forum/discussao.html', context)

def topico(request, discussao_titulo, topico_id):
    #pegando o topico de acordo com a url, para a discussão em questão
    try:
        topico = Topico.objects.get(pk = topico_id)
    except Topico.DoesNotExist:
        raise Http404("Tópico não existe nesta discussão.")
    
    form = RespostaForm(request.POST or None)
    #import ipdb; ipdb.set_trace()
    if form.is_valid():        
        form.save()
    
    resposta_lista = Resposta.objects.filter(topico_fk__id = topico_id)
    context = {'topico':topico, 'resposta_lista': resposta_lista, 'form':form}
    return render(request, 'forum/topico.html', context)

def criar_topico(request, discussao_titulo):
    try:    
        discussao = Discussao.objects.get(titulo = discussao_titulo)
    except Discussao.DoesNotExist:
        pass

    form = TopicoForm(request.POST or None)
    #import ipdb; ipdb.set_trace()
    if form.is_valid():        
        form.save()
        return redirect("../")
    
    context = {'discussao': discussao, 'form': form}
    return render(request, 'forum/criar_topico.html', context)


