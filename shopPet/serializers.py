from django.conf import settings
from rest_framework import serializers
from.models import shopPet

class shopSerilizer(serializers.ModelSerializer):
    img =serializers.SerializerMethodField()
    class Meta:
        model = shopPet
        fields = ('img','title','prize','des','recstore')
    def get_img(self, blog):
        return blog.img.url