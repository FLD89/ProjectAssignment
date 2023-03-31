from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from home.models import SoftwareEngineer, SoftwareTraining
from engineer_update.forms import UpdateEngineerForm
from training_create.forms import CreateTrainingForm


def engineer_read(request):
    engineers = SoftwareEngineer.objects.all()
    trainings = SoftwareTraining.objects.all()
    # Passes additional context data for use within the html template file
    context = {
        'engineers': engineers,
        'trainings': trainings
    }
    return render(
        request,
        'engineer_read/engineer_read.html',
        context
    )


def engineer_update(request, engineer_id):
    if request.method == 'POST':
        form = UpdateEngineerForm(request.POST)

        # Validates input data using logic in associated forms.py file
        if form.is_valid():
            engineer = SoftwareEngineer.objects.get(engineer_id=engineer_id)
            data = form.cleaned_data
            engineer.engineer_name = data['engineer_name']
            engineer.save(update_fields=['engineer_name'])
            return HttpResponseRedirect(reverse('engineer_read'))

        else:
            return render(
                request,
                'engineer_update/engineer_update.html',
                {'form': form}
            )

    engineer = SoftwareEngineer.objects.get(engineer_id=engineer_id)
    # Pre-populates the form with the data of the record being updated
    form = UpdateEngineerForm(initial={'engineer_name': engineer.engineer_name})
    return render(
        request,
        'engineer_update/engineer_update.html',
        {'form': form}
    )


def training_create(request, engineer_id):
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
            engineers = SoftwareEngineer.objects.all()
            return render(
                request,
                'training_create/training_create.html',
                # Passes additional context data for use within the html template file
                {'form': form,
                 'engineer_id': engineer_id,
                 'engineers': engineers,
                 }
            )

    # Pre-populates the form with the data of the record being updated
    form = CreateTrainingForm(initial={"engineer_id": engineer_id})
    engineers = SoftwareEngineer.objects.all()
    return render(
        request,
        'training_create/training_create.html',
        # Passes additional context data for use within the html template file
        {'form': form,
         'engineer_id': engineer_id,
         'engineers': engineers,
         }
    )



