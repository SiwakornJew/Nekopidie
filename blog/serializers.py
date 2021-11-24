from rest_framework import serializers
from.models import Blogs

class BlogsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'