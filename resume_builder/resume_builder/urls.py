from django.contrib import admin
from django.urls import path, include
from resume.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('resume/', include('resume.urls')),
]
