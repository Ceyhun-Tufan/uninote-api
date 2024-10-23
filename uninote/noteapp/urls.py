from django.urls import path 
from noteapp.views import HelloWorldView

urlpatterns = [
    path('hello/',HelloWorldView.as_view())
]