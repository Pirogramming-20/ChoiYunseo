from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_list),
    path('<int:pk>', views.reviews_read),
    path('create', views.reviews_create),
    path('<int:pk>/update', views.reviews_update),
    path('<int:pk>/delete', views.reviews_delete),
]