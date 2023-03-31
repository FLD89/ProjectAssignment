from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from engineer_create.forms import CreateEngineerForm
from home.models import SoftwareEngineer


def engineer_create(request):
    if request.method == 'POST':
        form = CreateEngineerForm(request.POST)

        # Validates input data using logic in associated forms.py file
        if form.is_valid():
            data = form.cleaned_data
            software_engineer = SoftwareEngineer(
                engineer_id=data['engineer_id'],
                engineer_name=data['engineer_name'],
            )
            software_engineer.save()
            return HttpResponseRedirect(reverse('engineer_read'))

        else:
            return render(
                request,
                'engineer_create/engineer_create.html',
                {'form': form}
            )

    form = CreateEngineerForm(None)
    return render(
        request,
        'engineer_create/engineer_create.html',
        {'form': form}
    )


