from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from.serializers import foodSerilizer
from.models import foodCat
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/foodCats-list/',
        'Detail View': '/foodCats-detail/<int:id>/',
        'Create': '/foodCats-create/',
        'Update': '/foodCats-update/<int:id>/',
        'Delete': '/foodCats-detail/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products = foodCat.objects.all()
    print(products)
    serializers = foodSerilizer(products,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewfoodCat(request,pk):
    products = foodCat.objects.get(id=pk)
    serializers = foodSerilizer(products,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def CreatefoodCat(request):
    serializers = foodSerilizer(data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['POST'])
def updatefoodCat(request,pk):
    product = foodCat.objects.get(id=pk)
    serializers = foodSerilizer(instance=product, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['GET'])
def deletefoodCat(request,pk):
    product = foodCat.objects.get(id=pk)
    product.delete()

    return Response('Item delete successfully')