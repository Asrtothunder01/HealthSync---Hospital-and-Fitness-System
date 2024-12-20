"""
URL configuration for hospital project.

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
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/',include('user.urls')),

    path('patient/',include('patient.urls')),

    path('doctor/',include('doctor.urls')),

    path('appointment/',include('appointment.urls')),

    path('medical/',include('records.urls')),

    path('prescription/',include('prescription.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/auth/',include('dj_rest_auth.urls')),

    path('account/',include('allauth.urls')),

    path('api/auth/register/',include('dj_rest_auth.registration.urls')),

    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('api/redoc/', SpectacularRedocView.as_view(url_name = 'schema'),name = 'redoc'),




]
