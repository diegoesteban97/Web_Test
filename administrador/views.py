from django.shortcuts import render
from .models import Producto, User
# Create your views here.

def index(request):
    administrador=Producto.objects.all()
    context={"administrador":administrador}
    return render(request, 'html/index.html', context)

def calendario(request):
    return render(request, "html/calendario.html")

def buscar(request):
    return render(request, "html/explora.html")

def login(request):
    return render(request, "html/login.html")

def noticias(request):
    return render(request, "html/noticias.html")

def productos(request):
    return render(request, "html/producto.html")

def registrarse(request):
    return render(request, "html/registro.html")

def videos(request):
    return render(request, "html/videos.html")

def crud(request):
    administrador = User.objects.all()
    context = {'administrador': administrador }
    return render(request, 'html/mantenedor.html', context)

def mantenedor_del(request,pk):
    context={}
    try:
        user=User.objects.get(usuario=pk)
        
        user.delete()
        mensaje="Usuario eliminado"
        administrador = User.objects.all()
        context = {'administrador': administrador, 'mensaje': mensaje}
        return render(request, 'html/mantenedor.html', context)
    except:
        mensaje="Usuario no existe"
        administrador = User.objects.all()
        context = {'administrador': administrador, 'mensaje': mensaje}
        return render(request, 'html/mantenedor.html', context)
    


   