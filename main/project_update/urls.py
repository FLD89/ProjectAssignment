from django.urls import path
from project_update import views


urlpatterns = [
    path('project_update/<str:project_id>', views.project_update, name='project_update'),
]