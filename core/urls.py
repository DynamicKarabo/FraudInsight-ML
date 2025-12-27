from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This connects the project to your dashboard app
    path('dashboard/', include('dashboard.urls')), 
]