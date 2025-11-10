from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/nuevo/', views.nuevo_proyecto, name='nuevo_proyecto'),
]

