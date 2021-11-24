from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    des = models.TextField()
    img = models.ImageField(upload_to="blogsImages",blank=True)


    def __str__(self):
        return self.title
