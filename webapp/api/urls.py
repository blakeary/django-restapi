from django.urls import path
from . import views

urlpatterns = [
    path('wiki', views.wiki_page, name='wiki-page'),
]