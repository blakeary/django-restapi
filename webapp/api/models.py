from django.db import models
from django.contrib.auth.models import User


class Wiki(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE, related_name='categories')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = 'categories'    

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    published_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='published_pages')

    def __str__(self):
        return self.title
