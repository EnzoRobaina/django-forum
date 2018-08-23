from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import Http404
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

@method_decorator(login_required, name='dispatch')
class Account(View):
    
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        user_topicos = Topico.objects.filter(autor=request.user)
        context = {'user_topicos':user_topicos, 'form':form}            
        return render(request, 'forum/account.html', context)

    def post(self, request):
        form = UserUpdateForm(request.POST or None, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account')
        context = {'form':form}            
        return render(request, 'forum/account.html', context)
    #import ipdb; ipdb.set_trace()

def log(request):
    #define a next url caso exista
    next_url = request.GET.get("next")

    if request.method == 'POST':
        #pega os dados do usuario para autenticar
        username = request.POST.get('username')
        password = request.POST.get('password')

        #autentica o usuario em questao
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
    form = UserForm(request.POST, request.FILES or None)

    if form.is_valid():   
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        #funcao propria do modelo User que define a senha do usuario em questao
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
    
    context = {'form':form}            
    return render(request, 'forum/registrar.html', context)

@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/account')
        else:
            messages.error(request, 'Preencha a senha corretamente!')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form':form}
    return render(request, 'forum/update_password.html', context)

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

    #funcionamento da barra de pesquisa

    #recebe o valor a ser pesquisado e retorna os objetos que o contem
    pesquisa = request.GET.get("pesquisa")
    if pesquisa:
        topicos_lista = Topico.objects.filter(Q(titulo__icontains=pesquisa) | Q(texto__icontains=pesquisa), Q(discussao_fk__titulo = discussao_titulo))

    #caso nao haja nada na barra de pesquisa, mostra todos os objetos Topico  
    else:
        try:
            Discussao.objects.get(titulo=discussao_titulo)
        except Discussao.DoesNotExist:
            raise Http404("Discussão não existe")
        
        topicos_lista = Topico.objects.filter(discussao_fk__titulo = discussao_titulo).order_by('-data_postagem')
    context = {'topicos_lista':topicos_lista, 'quantidade_respostas':quantidade_respostas}
    return render(request, 'forum/discussao.html', context)

def topico(request, discussao_titulo, topico_id):
    path = request.path    
    #pegando o topico de acordo com a url, para a discussão em questão
    try:
        topico = Topico.objects.get(pk = topico_id)
    except Topico.DoesNotExist:
        raise Http404("Tópico não existe nesta discussão.")
    
    form = RespostaForm(request.POST or None)
    
    if form.is_valid():
        user = request.user
        #import ipdb; ipdb.set_trace()
        user.replies += 1
        user.save()               
        form.save()
        return redirect(path)
    
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
        user = request.user
        user.posts += 1
        user.save()        
        form.save()
        return redirect('../')
    
    context = {'discussao': discussao, 'form': form}
    return render(request, 'forum/criar_topico.html', context)


