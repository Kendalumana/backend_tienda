
from django.db import models

class User (models.Model):

    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    profile = models.TextField(max_length=500)

   
