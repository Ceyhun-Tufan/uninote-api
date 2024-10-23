
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('auth/',include('authapp.urls')),
    path('note/api/',include('noteapp.urls')),
    path('admin/', admin.site.urls),
]
