from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('home.urls')),
    path('engineer_create/', include('engineer_create.urls')),
    path('engineer_read/', include('engineer_read.urls')),
    path('engineer_update/<str:engineer_id>', include('engineer_update.urls')),
    path('training_create/', include('training_create.urls')),
    path('training_read/', include('training_read.urls')),
    path('training_update/<str:training_id>', include('training_update.urls')),
    path('project_create/', include('project_create.urls')),
    path('project_read/', include('project_read.urls')),
    path('project_update/<str:project_id>', include('project_update.urls')),
    path('assignment_create/<str:project_id>', include('assignment_create.urls')),
    path('assignment_read/', include('assignment_read.urls')),
    path('assignment_update/<str:lookup_id>', include('assignment_update.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
