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
    #path('opciones/pasteleria_opciones', pasteleria_opciones, name = 'pasteleria_opciones'),
    path('pasteleria/', pasteleria, name = 'pasteleria'),
    path('opciones/', opciones, name = 'opciones'),
    path('targetas_form/', targetas_form, name = 'targetas_form'),

    path('ckeditor/',include('ckeditor_uploader.urls')),
    
    path('agregar_pasteleria/', agregar_pasteleria, name = 'agregar_pasteleria'),
    path('eliminar_pasteleria_template/', eliminar_pasteleria_template, name = 'eliminar_pasteleria_template'),
    path('eliminar_pasteleria/<id>/', eliminar_pasteleria, name = 'eliminar_pasteleria'),
    path('editar_pasteleria/<id>/',editar_pasteleria, name= 'editar_pasteleria'),
    path('editar_pasteleria_img/<id>/',editar_pasteleria_img, name= 'editar_pasteleria_img'),
    

    path('agregar_brunch/',agregar_brunch, name = 'agregar_brunch'),
    path('editar_brunch/<id>/',editar_brunch, name = 'editar_brunch'),
    path('editar_brunch_img/<id>/',editar_brunch_img, name= 'editar_brunch_img'),
    path('eliminar_brunch_template/',eliminar_brunch_template,name = 'eliminar_brunch_template'),
    path('eliminar_brunch/<id>/',eliminar_brunch,name = 'eliminar_brunch'),
    

    path('agregar_salados/', agregar_salados, name= 'agregar_salados'),
    path('editar_salados/<id>/',editar_salados, name = 'editar_salados'),
    path('editar_salados_img/<id>/',editar_salados_img, name= 'editar_salados_img'),
    path('eliminar_salados_template',eliminar_salados_template,name = 'eliminar_salados_template'),
    path('eliminar_salados/<id>/',eliminar_salados,name = 'eliminar_salados'),

    path('agregar_bebidas/', agregar_bebidas, name= 'agregar_bebidas'),
    path('editar_bebidas/<id>/', editar_bebidas, name='editar_bebidas'),
    path('editar_bebidas_img/<id>/',editar_bebidas_img, name= 'editar_bebidas_img'),
    path('eliminar_bebidas_template/', eliminar_bebidas_template, name = 'eliminar_bebidas_template'),
    path('eliminar_bebidas/<id>/',eliminar_bebidas, name= 'eliminar_bebidas'),



    path('agregar_cafes/', agregar_cafes, name= 'agregar_cafes'),
    path('editar_cafes/<id>/', editar_cafes, name='editar_cafes'),
    path('editar_cafes_img/<id>/',editar_cafes_img, name= 'editar_cafes_img'),
    path('eliminar_cafes_template/', eliminar_cafes_template, name='eliminar_cafe_template'),
    path('eliminar_cafes/<id>/',eliminar_cafes, name= 'eliminar_cafes'),

    path('agregar_populares/',agregar_populares, name= 'agregar_populares'),
    path('editar_populares/<id>/', editar_populares, name='editar_populares'),
    path('editar_populares_img/<id>/',editar_populares_img, name= 'editar_populares_img'),
    path('eliminar_populares_template/', eliminar_populares_template, name='eliminar_populares_template'),
    path('eliminar_populares/<id>/',eliminar_populares,name = 'eliminar_populares'),


    path('opciones_pasteleria',opciones_pasteleria,name = 'opciones_pasteleria'),
    path('opciones_brunch',opciones_brunch,name = 'opciones_brunch'),
    path('opciones_bebidas',opciones_bebidas,name = 'opciones_bebidas'),
    path('opciones_salados',opciones_salados,name = 'opciones_salados'),
    path('opciones_cafes',opciones_cafes,name = 'opciones_cafes'),
    path('opciones_populares',opciones_populares,name = 'opciones_populares'),


]+static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
