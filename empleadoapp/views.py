from django.shortcuts import render
from .models import Templeado
# Create your views here.

def index_empleadoapp(request):
    return render(request,'index.html')
    
def crear_empleadoapp(request):
    if request.method=='POST':
        nombre=request.POST['nombre']
        url=request.POST['url']
        Templeado.objects.create(nombre=nombre,url=url) #orm
        # empleado=Templeado()
        # empleado.nombre=nombre
        # empleado.url=url
        # empleado.save()
    return render(request,'empleadoapp/crear.html')