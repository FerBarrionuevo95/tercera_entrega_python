from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_post, name='crear'),
    path('buscar/', views.buscar, name='buscar'),

]