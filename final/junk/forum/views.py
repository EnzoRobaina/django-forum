from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import Http404
from django.utils import timezone

def main(request):
    topicos_lista = Topico.objects.order_by('-data_postagem')
    context = {'topicos_lista': topicos_lista}
    return render(request, 'forum/main.html', context)

def index(request):
    return render(request, 'forum/index.html')

def criar_topico(request):
    form = TopicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {'form': form}
    return render(request, 'forum/criar_topico.html', context)
    
    
    #if request.method == 'POST':
    #    form = TopicoForm(request.POST)
    #    if form.is_valid():
    #        new_topico = Topico(autor = request.POST['autor'], texto = request.POST['texto'], titulo = request.POST['titulo'])
    #        new_topico.save()
    #        return redirect('main.html')
    #else:
    #    form = TopicoForm()
    

def topico(request, topico_id):
    try:
        topico = Topico.objects.get(pk=topico_id)
    except Topico.DoesNotExist:
        raise Http404("Topico não existe.")

    form = RespostaForm(request.POST or None)
    if form.is_valid():
        resposta = form.save(commit=False)
        resposta.topico_fk = topico
        resposta.save()
        #new_resposta = Resposta(autor = request.POST['autor'], texto = request.POST['texto'], topico_fk = topico)
        #new_resposta.save()
        return redirect("../%s" %topico.id)
    resposta_lista = Resposta.objects.filter(topico_fk__id=topico_id)    
    context = {'topico':topico,'resposta_lista':resposta_lista, 'form':form}
    return render(request, 'forum/topico.html', context)