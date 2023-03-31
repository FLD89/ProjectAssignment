from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from training_create.forms import CreateTrainingForm
from home.models import SoftwareTraining, SoftwareEngineer


def training_create(request):
    if request.method == 'POST':
        form = CreateTrainingForm(request.POST)

        # Validates input data using logic in associated forms.py file
        if form.is_valid():
            data = form.cleaned_data
            software_training = SoftwareTraining(
                engineer_id=SoftwareEngineer.objects.get(engineer_id=data['engineer_id']),
                software=data['software'],
            )
            software_training.save()
            return HttpResponseRedirect(reverse('engineer_read'))

        else:
            return render(
                request,
                'training_create/training_create.html',
                {'form': form}
            )

    form = CreateTrainingForm(None)
    engineers = SoftwareEngineer.objects.all()
    return render(
        request,
        'training_create/training_create.html',
        # Passes additional context data for use within the html template file
        {'form': form,
         'engineers': engineers}
    )

