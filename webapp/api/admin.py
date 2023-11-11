from django.contrib import admin
from . models import Wiki, Category, Page

admin.site.register(Wiki)
admin.site.register(Category)
admin.site.register(Page)