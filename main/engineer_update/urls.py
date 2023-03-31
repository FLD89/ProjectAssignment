from django.urls import path
from engineer_update import views


urlpatterns = [
    path('engineer_update/<str:engineer_id>', views.engineer_update, name='engineer_update'),
]