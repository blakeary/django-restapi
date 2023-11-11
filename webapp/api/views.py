from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Page
from . serializers import RegistrationSerializer, PageSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        
        # Serialize the data
        serializer = RegistrationSerializer(data=request.data)
        
        # Create a response
        data = {}
        
        # Validate the data
        if serializer.is_valid():
            
            # Save the data
            user = serializer.save()
            
            # Return a response
            data['response'] = "Successfully registered a new user"
            
            # Return the user's token            
            auth_token = Token.objects.get(user=user).key
            
            # Return the token
            data['token'] = auth_token
        
        else:
            
            # Return an error
            data = serializer.errors
            
        # Return a response
        return Response(data)

@api_view(['GET'])
def get_pages(request):
    if request.method == 'GET':

        # Get all pages
        pages = Page.objects.all()
        
        # Serialize the data
        serializer = PageSerializer(pages, many=True)
        
        # Return a response
        return Response(serializer.data)
    
    # Return an error
    return Response(serializer.errors)

@api_view(['GET'])
def get_page(request, pk):
    try:
        if request.method == 'GET':
            
            # Get the page
            page = Page.objects.get(id=pk)
            
            # Serialize the data
            serializer = PageSerializer(page, many=False)
            
            # Return a response
            return Response(serializer.data)
        
        # Return an error
        return Response(serializer.errors)
    
    except:

        # Return an error
        return Response({"message": "Page does not exist"})

@api_view(['POST'])
def create_page(request):
    if request.method == 'POST':
        
        # Serialize the data
        serializer = PageSerializer(data=request.data)
        
        # Validate the data
        if serializer.is_valid():
            
            # Save the data
            serializer.save()
            
            # Return a response
            return Response(serializer.data)
        
        # Return an error
        return Response(serializer.errors)

@api_view(['PUT'])
def update_page(request, pk):
    try:
        if request.method == 'PUT':
            
            # Get the page
            page = Page.objects.get(id=pk)
            
            # Serialize the data
            serializer = PageSerializer(instance=page, data=request.data)
            
            # Validate the data
            if serializer.is_valid():
                
                # Save the data
                serializer.save()
                
                # Return a response
                return Response(serializer.data)
            
            # Return an error
            return Response(serializer.errors)
        
    except:

        # Return an error
        return Response({"message": "Page does not exist"})
    
@api_view(['PATCH'])
def partial_update_page(request, pk):
    try:
        if request.method == 'PATCH':
            
            # Get the page
            page = Page.objects.get(id=pk)
            
            # Serialize the data
            serializer = PageSerializer(instance=page, data=request.data, partial=True)
            
            # Validate the data
            if serializer.is_valid():
                
                # Save the data
                serializer.save()
                
                # Return a response
                return Response(serializer.data)
            
            # Return an error
            return Response(serializer.errors)
        
    except:

        # Return an error
        return Response({"message": "Page does not exist"})
    
@api_view(['DELETE'])
def delete_page(request, pk):
    try:
        if request.method == 'DELETE':
            
            # Get the page
            page = Page.objects.get(id=pk)
            
            # Delete the page
            page.delete()
            
            # Return a response
            return Response({"message": "Page deleted"})
        
    except:

        # Return an error
        return Response({"message": "Page does not exist"})