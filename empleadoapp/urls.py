from django.urls import path

from .views import *

urlpatterns = [
    
    path('',index_empleadoapp), #127.0.0.1:8000
    path('crear',crear_empleadoapp) #127.0.0.1:8000/crear
]