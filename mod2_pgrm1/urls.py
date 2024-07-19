from django.urls import path
from . import views

urlpatterns = [
    path('fruit/', views.fruit_list),
    path('student/', views.student_list),
]
