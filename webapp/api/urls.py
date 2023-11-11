from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
    path('register', views.register, name='register'),
    path('get-pages', views.get_pages, name='get-pages'),
    path('get-page/<int:pk>', views.get_page, name='get-page'),
    path('create-page', views.create_page, name='create-page'),
    path('update-page/<int:pk>', views.update_page, name='update-page'),
    path('partial-update-page/<int:pk>', views.partial_update_page, name='partial-update-page'),
    path('delete-page/<int:pk>', views.delete_page, name='delete-page'),
]