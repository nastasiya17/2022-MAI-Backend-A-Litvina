from unicodedata import category
from category.models import Category
from category.serializers  import CategorySerializer

from rest_framework import status, viewsets
from rest_framework.response import Response

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def index(request):
    http = \
    """
    <html lang="ru">
    <head>
        <title>Веб-сервер</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></meta>
    </head>
    <body>
        <h1> Hello, it's Jango!</h1>
        <p><a href="/admin/">Доступ администратора</a></p>
    </html>
    """
    return HttpResponse(http)

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            category = Category()
            category.name = serializer.validated_data["name"]
            category.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        
        category = None
        try:
            category = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = CategorySerializer(category)
        return Response(serializer.data)
