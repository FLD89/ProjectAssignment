from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from home.models import SoftwareTraining, SoftwareEngineer
from training_update.forms import UpdateTrainingForm


def training_read(request):
    trainings = SoftwareTraining.objects.all()
    # Passes additional context data for use within the html template file
    context = {
        'trainings': trainings
    }
    return render(
        request,
        'training_read/training_read.html',
        context
    )


def training_update(request, training_id):
    if request.method == 'POST':
        form = UpdateTrainingForm(request.POST)

        # Validates input data using logic in associated forms.py file
        if form.is_valid():
            training = SoftwareTraining.objects.get(training_id=training_id)
            data = form.cleaned_data
            training.software = data['software']
            training.save(update_fields=['software'])
            return HttpResponseRedirect(reverse('training_read'))

        else:
            return render(
                request,
                'training_update/training_update.html',
                {'form': form}
            )

    training = SoftwareTraining.objects.get(training_id=training_id)
    # Pre-populates the form with the data of the record being updated
    form = UpdateTrainingForm(initial={
        'engineer_id': training.engineer_id_id,
        'training_id': training_id
    })
    return render(
        request,
        'training_update/training_update.html',
        {'form': form}
    )


