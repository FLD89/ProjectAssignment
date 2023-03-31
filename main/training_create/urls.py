from django.urls import path
from training_create import views

urlpatterns = [
    path('training_create/', views.training_create, name='training_create'),
]