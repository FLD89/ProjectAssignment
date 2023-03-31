from django.contrib import admin
from .models import SoftwareEngineer
from .models import SoftwareTraining
from .models import Project
from .models import ProjectEngineerLookup

@admin.register(SoftwareEngineer)
class SoftwareEngineerAdmin(admin.ModelAdmin):
    list_display = ['engineer_id','engineer_name']

@admin.register(SoftwareTraining)
class SoftwareTrainingAdmin(admin.ModelAdmin):
    list_display = ['training_id','engineer_id','software']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id','project_name','software']

@admin.register(ProjectEngineerLookup)
class SoftwareEngineerAdmin(admin.ModelAdmin):
    list_display = ['lookup_id','engineer_id','project_id']
