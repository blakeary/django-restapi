from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Page
from . serializers import PageSerializer

@api_view(['GET'])
def wiki_page(request):
    if request.method == 'GET':

        # Get all pages
        pages = Page.objects.all()
        
        # Serialize the data
        serializer = PageSerializer(pages, many=True)
        
        return Response(serializer.data)