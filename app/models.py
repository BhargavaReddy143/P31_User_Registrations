from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    Address=models.TextField()
    Profile_pic=models.ImageField()
    username=models.OneToOneField(User, on_delete=models.CASCADE)