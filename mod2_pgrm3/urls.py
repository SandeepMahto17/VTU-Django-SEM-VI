from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list),
    path('register/<int:course_id>', views.register_student, name='register'),
]
