from django.db import models

class Usuario(models.Model):
    useario = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100) 
    repeat_password = models.CharField(max_length=100) 