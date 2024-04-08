from django.contrib import admin
from .models import Project, Study

# Register your models here.

#Para ver campos ocultos 'created' y 'updated'
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Study, ProjectAdmin)
