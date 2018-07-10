from django.db import models
from django.utils import timezone
# Create your models here.

class Topico(models.Model):
    titulo = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    texto = models.TextField()
    data_postagem = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Titulo: {}, Autor: {}, ID: {}'.format(self.titulo, self.autor, self.id)

class Resposta(models.Model):
    topico_fk = models.ForeignKey(Topico, on_delete=models.CASCADE)
    autor = models.CharField(max_length=20)
    texto = models.TextField()
    data_postagem = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Topico: {}, Autor: {}, ID: {}'.format(self.topico_fk.id, self.autor, self.id)

class Forum(models.Model):
    titulo = models.CharField(max_length=20)
    topico_fk = models.ForeignKey(Topico, on_delete=models.CASCADE)
    qtd_topicos = models.IntegerField(default = len(Topico.objects.filter(topico_fk__id=id)))

    def __str__(self):
        return 'Titulo: {}, Quantidade de tópicos: {}'.format(self.titulo, self.qtd_topicos)

    

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return 'ID: {}, Username: {}'.format(self.id, self.username)