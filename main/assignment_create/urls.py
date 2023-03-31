from django.urls import path
from assignment_create import views

urlpatterns = [
    path('assignment_create/<str:project_id>', views.assignment_create, name='assignment_create'),
]