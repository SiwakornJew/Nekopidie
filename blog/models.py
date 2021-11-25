from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    des = models.TextField()
    img = CloudinaryField('image')


    def __str__(self):
        return self.title
