from django.urls import path
from . import views

urlpatterns = [
    path('', views.datetime_with_offsets),
]
