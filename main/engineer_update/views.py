from django.shortcuts import render
from engineer_update.forms import UpdateEngineerForm


def engineer_update(request):
    form = UpdateEngineerForm()

    return render(
        request,
        'engineer_update/engineer_update.html',
        {'form': form}
    )