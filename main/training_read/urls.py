from django.urls import path
from training_read import views


urlpatterns = [
    path('training_read/', views.training_read, name='training_read'),
    path('training_update/<str:training_id>', views.training_update, name='training_update'),
]

