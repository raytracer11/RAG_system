from django.urls import path
from . import views

app_name = 'RAG'

urlpatterns = [
    # Add your URL patterns here
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
] 