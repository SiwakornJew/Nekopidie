from django.conf import settings
from rest_framework import serializers
from.models import  listCats

class catSerilizer(serializers.ModelSerializer):
    class Meta:
        model = listCats
        fields = '__all__'