from re import I, sub
from unicodedata import category
from urllib import request
from django.shortcuts import render
import json

from rest_framework.response import Response
from rest_framework import status

# Create your views here.


from django.shortcuts import HttpResponse
from django.urls import is_valid_path
from rest_framework.decorators import api_view

import api
from api.serializers import ItemSerializer
from .models import *
from django.core import serializers


@api_view(['GET'])
def getall(request):
    Item = Items.objects.all().values()
    # Item_json = serializers.serialize('json', Item)
    dicto = list(Item)
    Item_json = json.dumps(dicto)

    return HttpResponse(Item_json, content_type='application/json')
    


@api_view(['GET'])
def getcategory(request,cat):
    CatItem = Items.objects.filter(category=cat).values()
    dicto = list(CatItem)
    Item_json = json.dumps(dicto)
    return HttpResponse(Item_json, content_type='application/json')
   

@api_view(['GET'])
def getsubcategory(request,subcat):
    SubCatItem = Items.objects.filter(subcategory=subcat).values()
    dicto = list(SubCatItem)
    Item_json = json.dumps(dicto)
    return HttpResponse(Item_json, content_type='application/json')

@api_view(['GET'])
def getname(request,nam):
    NameItem = Items.objects.filter(name=nam).values()
    dicto = list(NameItem)
    Item_json = json.dumps(dicto)
    return HttpResponse(Item_json, content_type='application/json')



@api_view(['POST'])
def add_item(request):
    name = request.POST.get('name')
    category = request.POST.get('category')
    subcategory = request.POST.get('subcategory')
    amount = request.POST.get('amount')
    item_obj = Items(
        name = name,
        category = category,
        subcategory = subcategory,
        amount = amount
    )
    item_obj.save()
    return HttpResponse("Query Recieved! updates made")


@api_view(['PUT'])
def update_item(request):
    id = request.data.get('id')
    doc = Items.objects.get(pk=id)
    serializer = ItemSerializer(doc, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'data updated'})
    return Response(serializer.errors)