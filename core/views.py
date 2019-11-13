from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def galeria(request):
    return render(request,'core/galeria.html')    

def encabezado(request):
    return render(request,'core/encabezado.html')  

def evaluacion(request):
    return render(request,'core/evaluacion.html')  

def consulta(request):
    return render(request,'core/consulta.html')  