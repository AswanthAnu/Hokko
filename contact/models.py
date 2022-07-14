from platform import mac_ver
from django.db import models
from distutils.command.upload import upload
from unicodedata import name


# Create your models here.
class Giveaway(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to ='pics')
    desc= models.TextField()

    def __str__(self):
        return self.name
    
