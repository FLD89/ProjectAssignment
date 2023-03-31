from django.shortcuts import render
from assignment_update.forms import UpdateAssignmentForm


def assignment_update(request):
    form = UpdateAssignmentForm()
    return render(
        request,
        'assignment_update/assignment_update.html',
        {'form': form}
    )
