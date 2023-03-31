from django.urls import path
from assignment_read import views

urlpatterns = [
    path('assignment_read/', views.assignment_read, name='assignment_read'),
    path('assignment_update/<str:lookup_id>', views.assignment_update, name='assignment_update'),
]

