from rest_framework import serializers
from api.models import Wiki, Category, Page

class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ['category', 'title', 'content', 'created_at', 'updated_at', 'is_published', 'published_by']