from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.CharField(default='',max_length=200)
    password = models.CharField(default='',max_length=200)

    