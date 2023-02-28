from django.contrib import admin
from django.urls import path,include
from .views import * 
from django.conf.urls.static import static


urlpatterns = [
    path('inicio/', inicio, name = 'inicio'),
    path('brunch/', brunch, name = 'brunch'),
    path('salados/', salados, name = 'salados'),
    path('cafes/', cafes, name = 'cafes'),
    path('bebidas/', bebidas, name = 'bebidas'),
    path('opciones/pasteleria_opciones', pasteleria_opciones, name = 'pasteleria_opciones'),
    path('pasteleria/', pasteleria, name = 'pasteleria'),
    path('opciones/', opciones, name = 'opciones'),
    path('targetas_form/', targetas_form, name = 'targetas_form'),

    path('ckeditor/',include('ckeditor_uploader.urls')),
    
    path('agregar_pasteleria/', agregar_pasteleria, name = 'agregar_pasteleria'),
    path('eliminar_pasteleria_template/', eliminar_pasteleria_template, name = 'eliminar_pasteleria_template'),
    path('eliminar_pasteleria/<id>/', eliminar_pasteleria, name = 'eliminar_pasteleria'),
    path('editar_pasteleria/<id>/',editar_pasteleria, name= 'editar_pasteleria'),

    path('agregar_brunch/',agregar_brunch, name = 'agregar_brunch'),
    path('editar_brunch/<id>/',editar_brunch, name = 'editar_brunch'),
    path('eliminar_brunchs_template/',eliminar_brunchs_template,name = 'eliminar_brunchs_template'),
    path('eliminar_brunch/<id>/',eliminar_brunch,name = 'eliminar_brunch'),

    path('agregar_salados/', agregar_salados, name= 'agregar_salados'),
    path('editar_salados/<id>/',editar_salados, name = 'editar_salados'),
    path('eliminar_salados_template',eliminar_salados_template,name = 'eliminar_salados_template'),
    path('eliminar_salados/<id>/',eliminar_salados,name = 'eliminar_salados'),

    path('agregar_bebidas/', agregar_bebidas, name= 'agregar_bebidas'),
    path('eliminar_bebidas_template/', eliminar_bebidas_template, name = 'eliminar_bebidas_template'),

    path('editar_bebidas/<id>/', editar_bebidas, name='editar_bebidas'),
    path('eliminar_bebidas/<id>/',eliminar_bebidas, name= 'eliminar_bebidas'),



    path('agregar_cafes/', agregar_cafes, name= 'agregar_cafes'),
    path('editar_cafes/<id>/', editar_cafes, name='editar_cafes'),
    path('eliminar_cafes_template/', eliminar_cafes_template, name='eliminar_cafe_template'),
    path('eliminar_cafes/<id>/',eliminar_cafes, name= 'eliminar_cafes'),

]+static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
