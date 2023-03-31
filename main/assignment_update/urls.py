from django.urls import path
from assignment_update import views


urlpatterns = [
    path('assignment_update/<str:lookup_id>', views.assignment_update, name='assignment_update'),
]