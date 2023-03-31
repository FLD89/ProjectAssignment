from django.urls import path
from engineer_create import views

urlpatterns = [
    path('engineer_create/', views.engineer_create, name='engineer_create'),
]