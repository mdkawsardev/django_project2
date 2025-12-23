from django.urls import path
from . import views

urlpatterns = [
    path('project1/', views.project1, name='project1'),
]
