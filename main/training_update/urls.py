from django.urls import path
from training_update import views


urlpatterns = [
    path('training_update/<str:training_id>', views.training_update, name='training_update'),
]