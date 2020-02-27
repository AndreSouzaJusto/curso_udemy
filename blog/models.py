from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    status = ( ('rascunho','Rascunho'),
               ('publicado','Publicado')
    )

    title       = models.CharField(max_length=250)
    slug        = models.SlugField(max_length=250)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    text        = models.TextField()
    publicado   = models.DateTimeField(default=timezone.now())
    criado      = models.DateTimeField(auto_now_add=True)
    alterado    = models.DateTimeField(auto_now=True)
    status      = models.CharField(max_length=10,choices=status,default='rasscunho')

# Ordena por coluna de status
    class Meta:
        ordering = ('publicado',)


    def __str__(self):
        return self.title


# Create your models here.
