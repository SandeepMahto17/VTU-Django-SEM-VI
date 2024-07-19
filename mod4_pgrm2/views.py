from django.shortcuts import render
from .models import Student
from .utils import generate_csv_response, generate_pdf_response

def download_links(req):
    return render(req, 'download_links.html')

def generate_csv_view(request):
    queryset = Student.objects.all() # Get data from your models
    response = generate_csv_response(queryset, 'students_data')
    return response

def generate_pdf_view(request):
    queryset = Student.objects.all() # Get data from your models
    response = generate_pdf_response(queryset, 'students_data')
    return response
