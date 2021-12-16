from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    secret_friends = models.ManyToManyField('self', symmetrical=False, related_name='secret_followers')
    
