from django.urls import path
from project_create import views

urlpatterns = [
    path('project_create/', views.project_create, name='project_create'),
]