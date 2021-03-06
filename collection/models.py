from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)