from django.shortcuts import render
from portfolio.models import Project,Study
from django.conf import settings
from django.http import FileResponse
import os


def home(request):
    return render(request, 'index.html')

def about(request):
    projects = Project.objects.all()
    studys = Study.objects.all()
    return render(request, 'about.html', {'projects':projects, 'studys':studys})

def download_pdf(request):
    # Ruta al archivo PDF
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', 'cv_francisco_claveria.pdf')
    
    # Abrir el archivo PDF y devolverlo como una respuesta de archivo
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')