from django.db import models

class Orcamento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    whatsapp = models.CharField(max_length=11, null=False, blank=False)

# Create your models here.
