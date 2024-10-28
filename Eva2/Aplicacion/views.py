from django.shortcuts import render, redirect
from Aplicacion.forms import FormDoctor
from Aplicacion.models import Doctor
# Create your views here.

def index(request):
    return render(request,'index.html')

def listado_doctores(request):
    doctores = Doctor.objects.all()
    data = {'doctores':doctores}
    return render(request,'listado_doctores.html',data)

def registro_doctor(request):
    form = FormDoctor()
    if request.method == 'POST':
        form = FormDoctor(request.POST)
        if form.is_valid():
            form.save()
        return listado_doctores(request)
    
    data = {'form':form}
    return render(request,'registro_doctor.html',data)

def eliminar_doctor (request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('/listado_doctores')

def modificar_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    form = FormDoctor(instance=doctor)    
    if request.method == 'POST':
        form = FormDoctor(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
        return listado_doctores(request)
    data = {'form':form}
    return render(request,'registro_doctor.html',data)
    
        