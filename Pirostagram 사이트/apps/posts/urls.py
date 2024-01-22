from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'), 
    path('like_ajax/', like_ajax, name='like_ajax'),
    path('create_comment_ajax/',create_comment_ajax, name='create_comment_ajax')  
]