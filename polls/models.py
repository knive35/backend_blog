from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)
    content = models.CharField(max_length=200)