from django.shortcuts import render, redirect
from almendra_app.forms import *
from django.contrib import messages

from .models import *

# Create your views here.


def inicio (request):

    form = pasteleria_model.objects.all()
    form_brunch = brunch_model.objects.all()
    form_salados = salados_model.objects.all()
    form_bebidas = bebidas_model.objects.all()
    form_cafes  = cafes_model.objects.all()
    form_populares = populares_model.objects.all()
    
    return render (request,'almendra_app/inicio.html',{'form':form,
                                                'form_brunch':form_brunch,
                                                'form_salados': form_salados,
                                                'form_bebidas':form_bebidas,
                                                'form_cafes':form_cafes,
                                                'form_populares':form_populares
                                                })

def brunch (request):
    form_brunch = brunch_model.objects.all()
    form_populares = populares_model.objects.all()
    return render (request,'almendra_app/opciones/brunch/brunch.html',{'form_brunch':form_brunch,'form_populares':form_populares})

def eliminar_brunch_template (request):
    form_brunch= brunch_model.objects.all()
    return render (request,'almendra_app/opciones/brunch/eliminar_brunch_template.html',{'form_brunch':form_brunch})    


def salados(request):
    form_salados= salados_model.objects.all()
    form_populares= populares_model.objects.all()
    return render (request,'almendra_app/opciones/salados/salados.html',{ 'form_salados': form_salados,'form_populares':form_populares})

def eliminar_salados_template(request):
    form_salados= salados_model.objects.all()
    return render (request,'almendra_app/opciones/salados/eliminar_salados_template.html',{'form_salados':form_salados})    



def cafes (request):
    form_cafes= cafes_model.objects.all()
    form_populares= populares_model.objects.all()
    return render (request,'almendra_app/opciones/cafes/cafes.html',{ 'form_cafes':form_cafes,'form_populares':form_populares})

def eliminar_cafes_template(request):
    form_cafes= cafes_model.objects.all()
    return render (request,'almendra_app/opciones/cafes/eliminar_cafes_template.html',{'form_cafes':form_cafes})    

def bebidas (request):
    form_bebidas= bebidas_model.objects.all()
    form_populares= populares_model.objects.all()
    return render (request,'almendra_app/opciones/bebidas/bebidas.html',{ 'form_bebidas':form_bebidas,'form_populares':form_populares})

def eliminar_bebidas_template (request):
    form_bebidas= bebidas_model.objects.all()
    return render (request,'almendra_app/opciones/bebidas/eliminar_bebidas_template.html',{'form_bebidas':form_bebidas})    

def pasteleria (request):
    form = pasteleria_model.objects.all()
    form_populares= populares_model.objects.all()
    return render (request,'almendra_app/opciones/pasteleria/pasteleria.html',{'form': form,'form_populares':form_populares})    


def eliminar_pasteleria_template(request):
    form= populares_model.objects.all()
    return render (request,'almendra_app/opciones/populares/eliminar_populares_template.html',{'form':form})    

def eliminar_populares_template(request):
    form_cafes= cafes_model.objects.all()
    return render (request,'almendra_app/opciones/cafes/eliminar_cafes_template.html',{'form_cafes':form_cafes})    

def opciones (request):
    
    form = pasteleria_model.objects.all()
    form_brunch = brunch_model.objects.all()
    form_salados = salados_model.objects.all()
    form_bebidas = bebidas_model.objects.all()
    form_cafes = cafes_model.objects.all()
    form_populares = populares_model.objects.all()
    return render (request,'almendra_app/opciones/opciones.html',{'form':form,
                                                              'form_brunch':form_brunch,
                                                              'form_bebidas':form_bebidas,
                                                              'form_salados':form_salados,
                                                              'form_cafes':form_cafes,
                                                              'form_populares': form_populares})


def opciones_pasteleria(request):
    form = pasteleria_model.objects.all()
    return render (request,'almendra_app/opciones/pasteleria/opciones_pasteleria.html',{'form':form})

def opciones_brunch(request):
    form_brunch= brunch_model.objects.all()
    return render (request,'almendra_app/opciones/brunch/opciones_brunch.html',{'form_brunch':form_brunch,})
    
def opciones_bebidas(request):
    form_bebidas = bebidas_model.objects.all()
    return render (request,'almendra_app/opciones/bebidas/opciones_bebidas.html',{'form_bebidas':form_bebidas,})

def opciones_salados(request):
    form_salados = salados_model.objects.all()
    return render (request,'almendra_app/opciones/salados/opciones_salados.html',{'form_salados':form_salados,})  

def opciones_cafes(request):
    form_cafes = cafes_model.objects.all()
    return render (request,'almendra_app/opciones/cafes/opciones_cafes.html',{'form_cafes':form_cafes,}) 

def opciones_populares(request):
    form_populares = populares_model.objects.all()
    return render (request,'almendra_app/opciones/populares/opciones_populares.html',{'form_populares':form_populares,})      




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
            informacion = info.get('informacion')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            pasteleria_1 = pasteleria_model(imagen = imagen,
                                            titulo = titulo,
                                            descripcion = descripcion,
                                            informacion = informacion,
                                            precio = precio)
            pasteleria_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = pasteleria_form()
        return render (request, 'almendra_app/opciones/pasteleria/agregar_pasteleria.html',{'form':form})



def eliminar_pasteleria(request,id):
    elementos = pasteleria_model.objects.filter(id=id)
    if len(elementos)!=0:
        elemento=elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('opciones')


def editar_pasteleria_img(request,id):
    elemento = pasteleria_model.objects.get(id=id)
    if request.method =='POST':
        form = pasteleria_form (request.POST,request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen=info['imagen']

            elemento.save()
            messages.success(request,'¡Imagen modificada correctamente!')
            return redirect('opciones')
    else:
        form= pasteleria_form(initial = {
                                        'imagen':elemento.imagen,
                                        })        
        model = pasteleria_model.objects.all()               
        return render (request, 'almendra_app/opciones/pasteleria/editar_pasteleria_img.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})




def editar_pasteleria (request,id):
    elemento = pasteleria_model.objects.get(id = id)
    print(elemento)
    if request.method == 'POST':
        form = pasteleria_form(request.POST,request.FILES)
        if form.is_valid():
            info = form.cleaned_data
          
            elemento.titulo = info['titulo']
            elemento.descripcion = info ['descripcion']
            elemento.informacion = info['informacion']
            elemento.precio = info ['precio']

            elemento.save()
           

            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= pasteleria_form(initial = {
                                
                                'titulo':elemento.titulo,
                                'descripcion':elemento.descripcion,
                                'informacion':elemento.informacion,
                                'precio':elemento.precio
                                 })        
        model = pasteleria_model.objects.all()               
        return render (request, 'almendra_app/opciones/pasteleria/editar_pasteleria.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})





# BRUNCH

def agregar_brunch (request):
    if request.method == 'POST':
        formulario = brunch_form(request.POST ,request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data
            imagen = info.get ('imagen')
            titulo = info.get('titulo')
            informacion = informacion.get('informacion')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            brunch_1 = brunch_model(imagen = imagen,
                                            titulo = titulo,
                                            informacion=informacion,
                                            descripcion = descripcion,
                                            precio = precio)
            brunch_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return render (request,'almendra_app/opciones/opciones.html')
    else:
        form = brunch_form()
        return render (request, 'almendra_app/opciones/brunch/agregar_brunch.html',{'form':form})



def editar_brunch_img(request,id):
    elemento = brunch_model.objects.get(id=id)
    if request.method =='POST':
        form = brunch_form (request.POST,request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen=info['imagen']

            elemento.save()
            messages.success(request,'¡Imagen modificada correctamente!')
            return redirect('opciones')
    else:
        form= brunch_form(initial = {
                                        'imagen':elemento.imagen,
                                        })        
        model = brunch_model.objects.all()               
        return render (request, 'almendra_app/opciones/brunch/editar_brunch_img.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})


        

def editar_brunch (request,id):
    elemento = brunch_model.objects.get(id = id)
    if request.method == 'POST':
        form = brunch_form(request.POST ,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
        
            elemento.titulo = info['titulo']
            elemento.informacion = info['informacion']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
            
           
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= brunch_form(initial = {
                                
                                'titulo':elemento.titulo,
                                'informacion':elemento.informacion,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
        model = brunch_model.objects.all()               
        return render (request, 'almendra_app/opciones/brunch/editar_brunch.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})


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
            informacion = info.get('informacion')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            salados_1 = salados_model(imagen = imagen,
                                            titulo = titulo,
                                            informacion=informacion,
                                            descripcion = descripcion,
                                            precio = precio)
            salados_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = salados_form()
        return render (request, 'almendra_app/opciones/salados/agregar_salados.html',{'form':form})




def editar_salados_img(request,id):
    elemento = salados_model.objects.get(id=id)
    if request.method =='POST':
        form = salados_form (request.POST,request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen=info['imagen']

            elemento.save()
            messages.success(request,'¡Imagen modificada correctamente!')
            return redirect('opciones')
    else:
        form= salados_form(initial = {
                                        'imagen':elemento.imagen,
                                        })        
        model = salados_model.objects.all()               
        return render (request, 'almendra_app/opciones/salados/editar_salados_img.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})



def editar_salados(request,id):
    elemento = salados_model.objects.get(id = id)
    if request.method =='POST':
        form = salados_form(request.POST,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
       
            elemento.titulo = info['titulo']
            elemento.informacion = info['informacion']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= salados_form(initial = {
                               
                                'titulo':elemento.titulo,
                                'informacion':elemento.informacion,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
       
        return render (request, 'almendra_app/opciones/salados/editar_salados.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})

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
            informacion = info.get('informacion')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            bebidas_1 = bebidas_model(imagen = imagen,
                                            titulo = titulo,
                                            informacion=informacion,
                                            descripcion = descripcion,
                                            precio = precio)
            bebidas_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = bebidas_form()
        return render (request, 'almendra_app/opciones/bebidas/agregar_bebidas.html',{'form':form})



def editar_bebidas_img(request,id):
    elemento = bebidas_model.objects.get(id=id)
    if request.method =='POST':
        form = bebidas_form (request.POST,request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen=info['imagen']

            elemento.save()
            messages.success(request,'¡Imagen modificada correctamente!')
            return redirect('opciones')
    else:
        form= bebidas_form(initial = {
                                        'imagen':elemento.imagen,
                                        })        
        model = bebidas_model.objects.all()               
        return render (request, 'almendra_app/opciones/bebidas/editar_bebidas_img.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})


def editar_bebidas(request,id):
    elemento = bebidas_model.objects.get(id = id)
    if request.method =='POST':
        form = bebidas_form(request.POST,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
        
            elemento.titulo = info['titulo']
            elemento.informacion = info['informacion']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= bebidas_form(initial = {
                              
                                'titulo':elemento.titulo,
                                'informacion':elemento.informacion,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
       
        return render (request, 'almendra_app/opciones/bebidas/editar_bebidas.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})

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
            informacion = info.get('informacion')
            descripcion = info.get ('descripcion')
            precio = info.get('precio')

            cafes_1 = cafes_model(imagen = imagen,
                                            titulo = titulo,
                                            informacion=informacion,
                                            descripcion = descripcion,
                                            precio = precio)
            cafes_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = cafes_form()
        return render (request, 'almendra_app/opciones/cafes/agregar_cafes.html',{'form':form})



def editar_cafes_img(request,id):
    elemento = cafes_model.objects.get(id=id)
    if request.method =='POST':
        form = cafes_form (request.POST,request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen=info['imagen']

            elemento.save()
            messages.success(request,'¡Imagen modificada correctamente!')
            return redirect('opciones')
    else:
        form= cafes_form(initial = {
                                        'imagen':elemento.imagen,
                                        })        
        model = cafes_model.objects.all()               
        return render (request, 'almendra_app/opciones/cafes/editar_cafes_img.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})




def editar_cafes(request,id):
    elemento = cafes_model.objects.get(id = id)
    if request.method =='POST':
        form = cafes_form(request.POST,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
          
            elemento.titulo = info['titulo']
            elemento.informacion = info['informacion']
            elemento.descripcion = info ['descripcion']
            elemento.precio = info ['precio']

            elemento.save()
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= cafes_form(initial = {
                            
                                'titulo':elemento.titulo,
                                'informacion':elemento.informacion,
                                'descripcion':elemento.descripcion,
                                'precio':elemento.precio
                                 })        
       
        return render (request, 'almendra_app/opciones/cafes/editar_cafes.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})

        

def eliminar_cafes (request,id):
    elementos = cafes_model.objects.filter(id = id)
    if len (elementos)!=0:
        elemento = elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('opciones')         



#POPULARES

def agregar_populares (request):
    if request.method == 'POST':
        formulario = populares_form(request.POST,request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data
            imagen = info.get ('imagen')
            titulo = info.get('titulo')
            descripcion = info.get ('descripcion')
            informacion = info.get('informacion')
            precio = info.get('precio')

            populares_1 = populares_model(imagen = imagen,
                                            titulo = titulo,
                                            descripcion = descripcion,
                                            informacion=informacion,
                                            precio = precio)
            populares_1.save()
            
            messages.success (request,'¡Nuevo producto creado!')
            return redirect ('opciones')
    else:
        form = populares_form()
        return render (request, 'almendra_app/opciones/populares/agregar_populares.html',{'form':form})




def editar_populares_img(request,id):
    elemento = populares_model.objects.get(id=id)
    if request.method =='POST':
        form = populares_form (request.POST,request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            elemento.imagen=info['imagen']

            elemento.save()
            messages.success(request,'¡Imagen modificada correctamente!')
            return redirect('opciones')
    else:
        form= populares_form(initial = {
                                        'imagen':elemento.imagen,
                                        })        
        model = populares_model.objects.all()               
        return render (request, 'almendra_app/opciones/populares/editar_populares_img.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})


def editar_populares(request,id):
    elemento = populares_model.objects.get(id = id)
    if request.method =='POST':
        form = populares_form(request.POST,request.FILES or None)
        if form.is_valid():
            info = form.cleaned_data
           
            elemento.titulo = info['titulo']
           #elemento.descripcion = info ['descripcion']
            elemento.informacion = info ['informacion']
            elemento.precio = info ['precio']

            elemento.save()
            messages.success(request,'¡Producto modificado correctamente!')
            return redirect('opciones')
    else:
        form= populares_form(initial = {
                                
                                'titulo':elemento.titulo,
                               # 'descripcion':elemento.descripcion,
                                'informacion':elemento.informacion,
                                'precio':elemento.precio
                                 })        
       
        return render (request, 'almendra_app/opciones/populares/editar_populares.html',{'form':form,'id':elemento.id,'titulo':elemento.titulo})




def eliminar_populares (request,id):
    elementos = populares_model.objects.filter(id = id)
    if len (elementos)!=0:
        elemento = elementos[0]
        elemento.delete()
        messages.success(request,'¡Eliminado correctamente!')
    return redirect ('opciones')    