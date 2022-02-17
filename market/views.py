from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Products

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

def home(request):
    context = {
        "products": Products.objects.all(),
    }
    return render(request, "market/home.html", context)

@api_view(['GET'])
def apiview(request):
    api_urls = {
        'Products':'/product-list/',
        'Detail View':'/product-detail/<str:pk>/',
        'Create':'/product-create/',
        'Update':'/product-update/<str:pk>',
        'Delete':'/product-delete/<str:pk>/'
    }

    return Response(api_urls)

@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    products = Products.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET','POST'])
def product_update(request, pk):
    product = Products.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
def product_delete(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return Response('Product is deleted')