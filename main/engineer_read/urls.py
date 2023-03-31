from django.urls import path
from engineer_read import views


urlpatterns = [
    path('engineer_read/', views.engineer_read, name='engineer_read'),
    path('engineer_update/<str:engineer_id>', views.engineer_update, name='engineer_update'),
    path('training_create/<str:engineer_id>', views.training_create, name='training_create'),
]

