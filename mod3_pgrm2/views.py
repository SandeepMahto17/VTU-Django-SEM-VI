from django.shortcuts import render
from .forms import StudentForm

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            # If the project data is included in the form, save it to the student object
            student.project_topic = form.cleaned_data['project_topic']
            student.languages_used = form.cleaned_data['languages_used']
            student.duration = form.cleaned_data['duration']
            student.save()
            return render(request, 'student_created.html', {'student':student})
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

