from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from.serializers import catSerilizer
from.models import listCats
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/Cats-list/',
        'Detail View': '/Cats-detail/<int:id>/',
        'Create': '/Cats-create/',
        'Update': '/Cats-update/<int:id>/',
        'Delete': '/Cats-detail/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products = listCats.objects.all()
    print(products)
    serializers = catSerilizer(products,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def Viewlistcats(request,pk):
    products = listCats.objects.get(id=pk)
    serializers = catSerilizer(products,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def Createlistcats(request):
    serializers = catSerilizer(data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['POST'])
def updatelistcats(request,pk):
    product = listCats.objects.get(id=pk)
    serializers = catSerilizer(instance=product, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
def deletelistcats(request,pk):
    product = listCats.objects.get(id=pk)
    product.delete()

    return Response('Item delete successfully')