from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', height_field='', width_field='', blank=True)

def __str__(self):
        return 'ID: {}, username: {}'.format(self.id, self.username)

class Discussao(models.Model):
    titulo = (models.CharField(max_length=20))

    def __str__(self):
        return 'Titulo: {}'.format(self.titulo)

class Topico(models.Model):
    discussao_fk = models.ForeignKey(Discussao, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = RichTextField()
    data_postagem = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Titulo: {}, Autor: {}, ID: {}'.format(self.titulo, self.autor, self.id)

class Resposta(models.Model):
    topico_fk = models.ForeignKey(Topico, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = RichTextField()
    data_postagem = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Topico: {}, Autor: {}, ID: {}'.format(self.topico_fk.id, self.autor, self.id)

