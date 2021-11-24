from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogsSerilizer
from .models import Blogs
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/blog-list/',
        'Detail View': '/blog-detail/<int:id>/',
        'Create': '/blog-create/',
        'Update': '/blog-update/<int:id>/',
        'Delete': '/blog-detail/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    blogs = Blogs.objects.all()
    serializers =BlogsSerilizer(blogs,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewBlog(request,pk):
    blogs = Blogs.objects.get(id=pk)
    serializers =BlogsSerilizer(blogs,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def CreateBlog(request):
    serializers =BlogsSerilizer(data=request.data)
    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['POST'])
def updateBlog(request,pk):
    blog = Blogs.objects.get(id=pk)
    serializers =BlogsSerilizer(instance=blog, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
def deleteblog(request,pk):
    blog = Blogs.objects.get(id=pk)
    blog.delete()

    return Response('Item delete successfully')