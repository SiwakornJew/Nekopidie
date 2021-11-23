from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from.serializers import ProductSerilizer
from.models import Product
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>/',
        'Delete': '/product-detail/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializers =ProductSerilizer(products,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewProduct(request,pk):
    products = Product.objects.get(id=pk)
    serializers =ProductSerilizer(products,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def CreateProduct(request):
    serializers =ProductSerilizer(data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['POST'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializers =ProductSerilizer(instance=product, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Item delete successfully')