from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class listCats(models.Model):
    img = models.CharField(max_length=200,null=True , blank=True )
    title = models.CharField(max_length=200, null=False, blank=False)
    prize = models.CharField(max_length=200, null=True, blank=False)
    #recstore = models.CharField(max_length=200,null=True , blank=True )
    temperament =  models.CharField(max_length=200, null=True, blank=False)
    coat =  models.CharField(max_length=200, null=True, blank=False)
    coat_color = models.CharField(max_length=200, null=True, blank=False)
    body_type =  models.CharField(max_length=200, null=True, blank=False)
    lifespan = models.CharField(max_length=200, null=True, blank=False)
    weight = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return self.title