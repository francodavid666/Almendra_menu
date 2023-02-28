from django.shortcuts import render, redirect
from almendra_app.forms import *
from django.contrib import messages

from .models import *

# Create your views here.


def inicio (request):

    form = pasteleria_model.objects.all()
    form_salado = salados_model.objects.all()
    form_bebidas = bebidas_model.objects.all()
    form_cafes  = cafes_model.objects.all()
    return render (request,'almendra_app/inicio.html',{'form':form,
                                                'form_salado': form_salado,
                                                'form_bebidas':form_bebidas,
                                                'form_cafes':form_cafes
                                                })

def brunch (request):
    return render (request,'almendra_app/brunch.html')

def eliminar_brunchs_template (request):
    form_brunch= brunch_model.objects.all()
    return render (request,'almendra_app/opciones/brunchs/eliminar_brunchs_template.html',{'form_brunch':form_brunch})    


def salados(request):
    return render (request,'almendra_app/salados.html')

def eliminar_salados_template(request):
    form_salados= salados_model.objects.all()
    return render (request,'almendra_app/opciones/salados/eliminar_salados_template.html',{'form_salados':form_salados})    



def cafes (request):
    return render (request,'almendra_app/cafes.html')

def eliminar_cafes_template(request):
    form_cafes= cafes_model.objects.all()
    return render (request,'almendra_app/opciones/cafes/eliminar_cafes_template.html',{'form_cafes':form_cafes})    

def bebidas (request):
    return render (request,'almendra_app/bebidas.html')

def eliminar_bebidas_template (request):
    form_bebidas= bebidas_model.objects.all()
    return render (request,'almendra_app/opciones/bebidas/eliminar_bebidas_template.html',{'form_bebidas':form_bebidas})    

def pasteleria (request):
    form = pasteleria_model.objects.all()
    return render (request,'almendra_app/pasteleria.html',{'form': form})    


def eliminar_pasteleria_template(request):
    form= pasteleria_model.objects.all()
    return render (request,'almendra_app/opciones/pasteleria/eliminar_pasteleria_template.html',{'form':form})    


def opciones (request):
    
    form = pasteleria_model.objects.all()
    form_brunch = brunch_model.objects.all()
    form_salados = salados_model.objects.all()
    form_bebidas = bebidas_model.objects.all()
    form_cafes = cafes_model.objects.all()
    return render (request,'almendra_app/opciones/opciones.html',{'form':form,
                                                              'form_brunch':form_brunch,
                                                              'form_bebidas':form_bebidas,
                                                              'form_salados':form_salados,
                                                              'form_cafes':form_cafes})

def pasteleria_opciones (request):
    return render (request,'almendra_app/opciones/pasteleria_opciones.html')



def targetas_form (request):

    form = pasteleria_form()
    print(form)
    return render (request,'almendra_app/opciones/targetas_form.html',{'form':form})


#def agregar_pasteleria (request):
 #   return render (request,'almendra_app/opciones/agregar_pasteleria.html')

def agregar_pasteleria (request):
    if request.method == 'POST':
        formulario = pasteleria_form(request.POST,request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data
            imagen = info.get ('imagen')
            titulo = info.get('titulo')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            pasteleria_1 = pasteleria_model(imagen = imagen,
                                            titulo = titulo,
                                            descripcion = descripcion,
                                            precio = precio)
            pasteleria_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = pasteleria_form()
        return render (request, 'almendra_app/opciones/agregar_pasteleria.html',{'form':form})



def eliminar_pasteleria(request,id):
    elementos = pasteleria_model.objects.filter(id=id)
    if len(elementos)!=0:
        elemento=elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('opciones')


def editar_pasteleria (request,id):
    elemento = pasteleria_model.objects.get(id = id)
    print(elemento)
    if request.method == 'POST':
        form = pasteleria_form(request.POST,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen = info ['imagen']
            elemento.titulo = info['titulo']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
           

            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= pasteleria_form(initial = {
                                'imagen':elemento.imagen,
                                'titulo':elemento.titulo,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
        model = pasteleria_model.objects.all()               
        return render (request, 'almendra_app/opciones/editar_pasteleria.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})





# BRUNCH

def agregar_brunch (request):
    if request.method == 'POST':
        formulario = brunch_form(request.POST ,request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data
            imagen = info.get ('imagen')
            titulo = info.get('titulo')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            brunch_1 = brunch_model(imagen = imagen,
                                            titulo = titulo,
                                            descripcion = descripcion,
                                            precio = precio)
            brunch_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return render (request,'almendra_app/opciones/opciones.html')
    else:
        form = brunch_form()
        return render (request, 'almendra_app/opciones/agregar_brunch.html',{'form':form})



        

def editar_brunch (request,id):
    elemento = brunch_model.objects.get(id = id)
    if request.method == 'POST':
        form = brunch_form(request.POST ,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen = info ['imagen']
            elemento.titulo = info['titulo']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
            
           
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= brunch_form(initial = {
                                'imagen':elemento.imagen,
                                'titulo':elemento.titulo,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
        model = brunch_model.objects.all()               
        return render (request, 'almendra_app/opciones/editar_brunch.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})


def eliminar_brunch(request,id):
    elementos = brunch_model.objects.filter(id = id)
    if len(elementos)!=0:
        elemento = elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
        
    return redirect('opciones')


#SALADOS

def agregar_salados(request):
    if request.method == 'POST':
        formulario = salados_form(request.POST,request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data
            imagen = info.get ('imagen')
            titulo = info.get('titulo')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            salados_1 = salados_model(imagen = imagen,
                                            titulo = titulo,
                                            descripcion = descripcion,
                                            precio = precio)
            salados_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = salados_form()
        return render (request, 'almendra_app/opciones/agregar_salados.html',{'form':form})



def editar_salados(request,id):
    elemento = salados_model.objects.get(id = id)
    if request.method =='POST':
        form = salados_form(request.POST,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen = info ['imagen']
            elemento.titulo = info['titulo']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= salados_form(initial = {
                                'imagen':elemento.imagen,
                                'titulo':elemento.titulo,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
       
        return render (request, 'almendra_app/opciones/editar_salados.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})

def eliminar_salados (request,id):
    elementos = salados_model.objects.filter(id = id)
    if len (elementos)!=0:
        elemento = elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('opciones')

#BEBIDAS

def agregar_bebidas(request):
    if request.method == 'POST':
        formulario = bebidas_form(request.POST,request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data
            imagen = info.get ('imagen')
            titulo = info.get('titulo')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            bebidas_1 = bebidas_model(imagen = imagen,
                                            titulo = titulo,
                                            descripcion = descripcion,
                                            precio = precio)
            bebidas_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = bebidas_form()
        return render (request, 'almendra_app/opciones/agregar_bebidas.html',{'form':form})


def editar_bebidas(request,id):
    elemento = bebidas_model.objects.get(id = id)
    if request.method =='POST':
        form = bebidas_form(request.POST,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen = info ['imagen']
            elemento.titulo = info['titulo']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= bebidas_form(initial = {
                                'imagen':elemento.imagen,
                                'titulo':elemento.titulo,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
       
        return render (request, 'almendra_app/opciones/editar_bebidas.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})

def eliminar_bebidas (request,id):
    elementos = bebidas_model.objects.filter(id = id)
    if len (elementos)!=0:
        elemento = elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('opciones') 



#CAFES 


def agregar_cafes(request):
    if request.method == 'POST':
        formulario = cafes_form(request.POST,request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data
            imagen = info.get ('imagen')
            titulo = info.get('titulo')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            cafes_1 = cafes_model(imagen = imagen,
                                            titulo = titulo,
                                            descripcion = descripcion,
                                            precio = precio)
            cafes_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = cafes_form()
        return render (request, 'almendra_app/opciones/agregar_cafes.html',{'form':form})


def editar_cafes(request,id):
    elemento = cafes_model.objects.get(id = id)
    if request.method =='POST':
        form = cafes_form(request.POST,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen = info ['imagen']
            elemento.titulo = info['titulo']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= cafes_form(initial = {
                                'imagen':elemento.imagen,
                                'titulo':elemento.titulo,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
       
        return render (request, 'almendra_app/opciones/editar_cafes.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})

        

def eliminar_cafes (request,id):
    elementos = cafes_model.objects.filter(id = id)
    if len (elementos)!=0:
        elemento = elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('opciones')         