from django.db import models
from django.db.models.fields import CharField, URLField

class Paginas(models.Model):
    title = CharField(max_length=100)
    url = URLField(blank=True)
