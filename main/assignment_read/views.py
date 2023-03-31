from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from home.models import Project, ProjectEngineerLookup, SoftwareEngineer, SoftwareTraining
from assignment_update.forms import UpdateAssignmentForm


def assignment_read(request):
    assignments = ProjectEngineerLookup.objects.all()
    engineers = SoftwareEngineer.objects.all()
    projects = Project.objects.all()
    # Passes additional context data for use within the html template file
    context = {
        'assignments': assignments,
        'engineers': engineers,
        'projects': projects
    }
    return render(
        request,
        'assignment_read/assignment_read.html',
        context
    )


def assignment_update(request, lookup_id):
    if request.method == 'POST':
        form = UpdateAssignmentForm(request.POST)

        # Validates input data using logic in associated forms.py file
        if form.is_valid():
            assignment = ProjectEngineerLookup.objects.get(lookup_id=lookup_id)
            data = form.cleaned_data
            assignment.project_id_id = data['project_id']
            assignment.engineer_id_id = data['engineer_id']
            assignment.save(update_fields=['project_id_id', 'engineer_id_id'])
            return HttpResponseRedirect(reverse('assignment_read'))

        else:
            return render(
                request,
                'training_update/training_update.html',
                {'form': form}
            )

    assignment = ProjectEngineerLookup.objects.get(lookup_id=lookup_id)
    # Pre-populates the form with the data of the record being updated
    form = UpdateAssignmentForm(initial={
        'engineer_id': assignment.engineer_id_id,
        'project_id': assignment.project_id_id

    })
    lookup = ProjectEngineerLookup.objects.get(lookup_id=lookup_id)
    project = Project.objects.get(project_id=lookup.project_id_id)
    projects = Project.objects.all()
    engineers = SoftwareEngineer.objects.all()
    trainings = SoftwareTraining.objects.all()
    lookups = ProjectEngineerLookup.objects.all()
    # Passes additional context data for use within the html template file
    context = {
        'form': form,
        'lookup': lookup,
        'project': project,
        'projects': projects,
        'engineers': engineers,
        'trainings': trainings,
        'lookups': lookups,
    }
    return render(
        request,
        'assignment_update/assignment_update.html',
        context
    )
