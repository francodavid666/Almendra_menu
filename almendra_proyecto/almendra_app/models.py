from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class pasteleria_model (models.Model):

     imagen = models.ImageField(blank=True, null = True,upload_to='pasteleria/')
     titulo = models.CharField(max_length=50, blank = True, null = True)
     descripcion =  models.CharField(max_length=50, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)



class salados_model (models.Model):
     imagen = models.ImageField(blank=True, null = True,upload_to='salados/')
     titulo = models.CharField(max_length=50, blank = True, null = True)
     descripcion =  models.CharField(max_length=50, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)


class bebidas_model (models.Model):
     imagen = models.ImageField(blank=True, null = True,upload_to='bebidas/')
     titulo = models.CharField(max_length=50, blank = True, null = True)
     descripcion =  models.CharField(max_length=50, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)

   

class cafes_model(models.Model):
     imagen = models.ImageField(blank=True, null = True,upload_to='cafes/')
     titulo = models.CharField(max_length=50, blank = True, null = True)
     descripcion =  models.CharField(max_length=50, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)


class brunch_model(models.Model):
     imagen = models.ImageField(blank=True, null = True,upload_to='brunchs/')
     titulo = models.CharField(max_length=50, blank = True, null = True)
     descripcion = RichTextUploadingField(max_length=500, blank = True, null = True)
     precio = models.CharField(max_length=50, blank = True, null = True)
     
     


