from django.urls import path
from . import views

urlpatterns = [
    path('', views.project1, name='project1'),
]
