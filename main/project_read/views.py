from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from home.models import Project, SoftwareEngineer, ProjectEngineerLookup, SoftwareTraining
from project_update.forms import UpdateProjectForm
from assignment_create.forms import CreateAssignmentForm


def project_read(request):
    projects = Project.objects.all()
    engineers = SoftwareEngineer.objects.all()
    lookups = ProjectEngineerLookup.objects.all()
    # Passes additional context data for use within the html template file
    context = {
        'projects': projects,
        'engineers': engineers,
        'lookups': lookups
    }
    return render(
        request,
        'project_read/project_read.html',
        context
    )


def project_update(request, project_id):
    if request.method == 'POST':
        form = UpdateProjectForm(request.POST)

        # Validates input data using logic in associated forms.py file
        if form.is_valid():
            project = Project.objects.get(project_id=project_id)
            data = form.cleaned_data
            # Does not update if supplied values are blank
            if data['project_name']:
                project.project_name = data['project_name']
                project.save(update_fields=['project_name'])
            if data['software']:
                project.software = data['software']
                project.save(update_fields=['software'])
            return HttpResponseRedirect(reverse('project_read'))

        else:
            return render(
                request,
                'project_update/project_update.html',
                {'form': form}
            )

    project = Project.objects.get(project_id=project_id)
    # Pre-populates the form with the data of the record being updated
    form = UpdateProjectForm(initial={
        'project_name': project.project_name,
        'software': project.software,
        'project_id': project_id
    })
    return render(
        request,
        'project_update/project_update.html',
        {'form': form}
    )


def assignment_create(request, project_id):
    project = Project.objects.get(project_id=project_id)
    engineers = SoftwareEngineer.objects.all()
    trainings = SoftwareTraining.objects.all()
    lookups = ProjectEngineerLookup.objects.all()

    if request.method == 'POST':
        form = CreateAssignmentForm(request.POST)
        # Passes additional context data for use within the html template file
        context = {
            'form': form,
            'project': project,
            'engineers': engineers,
            'trainings': trainings,
            'lookups': lookups,
        }

        # Validates input data using logic in associated forms.py file
        if form.is_valid():
            data = form.cleaned_data
            project_engineer_lookup = ProjectEngineerLookup(
                engineer_id_id=data['engineer_id'],
                project_id_id=project_id
            )
            project_engineer_lookup.save()
            return HttpResponseRedirect(reverse('project_read'))

        else:
            return render(
                request,
                'assignment_create/assignment_create.html',
                context,
            )

    # Pre-populates the form with the data of the record being updated
    form = CreateAssignmentForm(initial={'project_id': project_id})
    # Passes additional context data for use within the html template file
    context = {
        'form': form,
        'project': project,
        'engineers': engineers,
        'trainings': trainings,
        'lookups': lookups,
    }

    return render(
        request,
        'assignment_create/assignment_create.html',
        context,
    )
