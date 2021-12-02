from django.conf import settings
from rest_framework import serializers
from.models import Blogs

class BlogsSerilizer(serializers.ModelSerializer):
    #img = serializers.SerializerMethodField()
    class Meta:
        model = Blogs
        fields = ('title','des','img')
    #def get_img(self, blog):
        #return blog.img.url
