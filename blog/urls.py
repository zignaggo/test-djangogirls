from django.urls import path
from . import views

# '' --> url raiz
urlpatterns = [
    path('', views.post_list, name='post_list'),
]