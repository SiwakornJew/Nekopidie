from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class shopPet(models.Model):
    img = models.CharField(max_length=200, null=True, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    prize = models.CharField(max_length=200, null=True, blank=False)
    des = models.TextField()
    recstore = models.CharField(max_length=200,null=True , blank=True )
    

    def __str__(self):
        return self.title