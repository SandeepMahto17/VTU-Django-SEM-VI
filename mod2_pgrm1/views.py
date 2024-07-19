from django.shortcuts import render
from .models import Fruit, Student

# Create your views here.
def fruit_list(request):
    fruits = Fruit.objects.all()
    return render(request, 'fruit_list.html',{'fruits':fruits})

def student_list(request):
    students = Student.objects.filter(selected=True)
    return render(request, 'student_list.html', {'students':students})
