from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    project_topic = forms.CharField(max_length=255)
    languages_used = forms.CharField(max_length=255)
    duration = forms.IntegerField()
    
    class Meta:
        model = Student
        fields = ['name', 'email'] # Include other fields from the Student model as needed

