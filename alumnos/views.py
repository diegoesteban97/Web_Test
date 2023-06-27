from django.shortcuts import render

from .models import Genero, Alumno
# Create your views here.


def index(request):
    alumnos=Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index2.html',context)




