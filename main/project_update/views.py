from django.shortcuts import render
from project_update.forms import UpdateProjectForm


def project_update(request):
    form = UpdateProjectForm()

    return render(
        request,
        'project_update/project_update.html',
        {'form': form}
    )