from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from.serializers import shopSerilizer
from.models import shopPet
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/Shop-list/',
        'Detail View': '/Shop-detail/<int:id>/',
        'Create': '/Shop-create/',
        'Update': '/Shop-update/<int:id>/',
        'Delete': '/Shop-detail/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products = shopPet.objects.all()
    print(products)
    serializers = shopSerilizer(products,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewProduct(request,pk):
    products = shopPet.objects.get(id=pk)
    serializers = shopSerilizer(products,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def CreateProduct(request):
    serializers = shopSerilizer(data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['POST'])
def updateProduct(request,pk):
    product = shopPet.objects.get(id=pk)
    serializers =shopSerilizer(instance=product, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
def deleteProduct(request,pk):
    product = shopPet.objects.get(id=pk)
    product.delete()

    return Response('Item delete successfully')