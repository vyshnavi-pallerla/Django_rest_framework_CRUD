from drf_spectacular.utils import extend_schema
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.core.paginator import Paginator

# Create your views here.
@api_view(['GET','POST'])
@extend_schema(responses=ProductSerializer)
def products(request, format= None):

    if request.method == 'GET':
        products = Products.objects.all()
        page = request.GET.get('page',1)
        page_size = 3
        paginator = Paginator( products, page_size)
        serializer = ProductSerializer(paginator.page(page), many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

    
@api_view(['GET', 'PUT', 'DELETE'])  
@extend_schema(responses=ProductSerializer)  
def product_detail(request,id, format= None):

    try:
        product = Products.objects.get(pk = id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)