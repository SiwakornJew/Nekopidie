from django.conf import settings
from rest_framework import serializers
from.models import foodCat

class foodSerilizer(serializers.ModelSerializer):
    #img =serializers.SerializerMethodField()
    class Meta:
        model = foodCat
        fields = ('img','title','prize','des','recstore')
    #def get_img(self, blog):
        #return blog.img.url