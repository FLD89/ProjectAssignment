from django.urls import path
from project_read import views


urlpatterns = [
    path('project_read/', views.project_read, name='project_read'),
    path('project_update/<str:project_id>', views.project_update, name='project_update'),
    path('assignment_create/<str:project_id>', views.assignment_create, name='assignment_create'),
]

