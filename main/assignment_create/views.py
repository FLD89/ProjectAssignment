from django.shortcuts import render
from assignment_create.forms import CreateAssignmentForm


def assignment_create(request):
    form = CreateAssignmentForm(None)
    return render(
        request,
        'project_create/project_create.html',
        {'form': form},
    )
