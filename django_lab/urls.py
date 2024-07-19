"""
URL configuration for django_lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mod1-3/', include('mod1_pgrm3.urls')),
    path('mod1-4/', include('mod1_pgrm4.urls')),
    path('mod2-1/', include('mod2_pgrm1.urls')),
    path('mod2-2/', include('mod2_pgrm2.urls')),
    path('mod2-3/', include('mod2_pgrm3.urls')),
    path('mod3-2/', include('mod3_pgrm2.urls')),
    path('mod4-1/', include('mod4_pgrm1.urls')),
    path('mod4-2/', include('mod4_pgrm2.urls')),
    path('mod5-1/', include('mod5_pgrm1.urls')),
    path('mod5-2/', include('mod5_pgrm2.urls')),
]
