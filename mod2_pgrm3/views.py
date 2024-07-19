from django.shortcuts import render
from .models import Course, Student

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses':courses})

def register_student(request, course_id):
    course = Course.objects.get(pk = course_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        student, created = course.students.get_or_create(name = name, email = email)

        if created:
            message = f"{student.name} registed successfully for {course.name}"
        else:
            message = f"{student.name} is already registered for {course.name}"

        return render(request, 'confirmation.html', {'message':message})

    return render(request, 'registration.html', {'course':course})

