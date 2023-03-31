from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from project_create.forms import CreateProjectForm
from home.models import Project


def project_create(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)

        # Validates input data using logic in associated forms.py file
        if form.is_valid():
            data = form.cleaned_data
            project = Project(
                project_name=data['project_name'],
                software=data['software'],
            )
            project.save()
            return HttpResponseRedirect(reverse('project_read'))

        else:
            return render(
                request,
                'project_create/project_create.html',
                {'form': form}
            )

    form = CreateProjectForm(None)
    return render(
        request,
        'project_create/project_create.html',
        {'form': form}
    )



