from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, Student

def registration_page(request):
    courses = Course.objects.all()
    return render(request, 'registration1.html', {'courses':courses})

def register_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course_id = request.POST.get('course')
        course = Course.objects.get(pk=course_id)
        student = Student.objects.create(name=name, email=email, course=course)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})