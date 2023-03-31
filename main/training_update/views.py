from django.shortcuts import render
from training_update.forms import UpdateTrainingForm


def training_update(request):
    form = UpdateTrainingForm()
    return render(
        request,
        'training_update/training_update.html',
        {'form': form}
    )
