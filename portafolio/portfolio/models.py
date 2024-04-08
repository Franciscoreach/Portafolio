from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects',verbose_name='Imagen')
    link = models.URLField(max_length=250, verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['created']

    def __str__(self):
        return self.title
    
class Study(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects',verbose_name='Imagen')
    link = models.URLField(max_length=250, verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')

    class Meta:
        verbose_name = 'estudio'
        verbose_name_plural = 'estudios'
        ordering = ['created']

    def __str__(self):
        return self.title