"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView

admin.site.site_header = "NCC Admin"
admin.site.site_title = "NCC Admin Portal"
admin.site.index_title = "Welcome to NCC Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', TemplateView.as_view(template_name='login.html'), name='404-url'),
    path('', include('tools.urls')),
    path('management/', include('management.urls'), name="management"),
    path('404error', TemplateView.as_view(template_name='404.html'), name='404-url'),
]