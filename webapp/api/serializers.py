from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Page

class RegistrationSerializer(serializers.ModelSerializer):
    
    # Add a field for the password confirmation
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}
        
    def save(self):
        
        # Create the user
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        
        # Get the password
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        # Check if passwords match
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        
        # Hash the password
        user.set_password(password)
        
        # Save the user
        user.save()
        
        # Return the user
        return user

class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ['id', 'category', 'title', 'content', 'created_at', 'updated_at', 'is_published', 'published_by']
        
