from showplace.models import Showplace
from showplace.serializers  import ShowplaceSerializer

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

class ShowplaceViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Showplace.objects.all()
        serializer = ShowplaceSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ShowplaceSerializer(data=request.data)
        
        if serializer.is_valid():
            showplace = Showplace()
            showplace.name = serializer.validated_data["name"]
            showplace.category = serializer.validated_data["category_id"]
            showplace.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset = Showplace.objects.all()
        
        showplace = None
        try:
            showplace = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = ShowplaceSerializer(showplace)
        return Response(serializer.data)