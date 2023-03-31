from django import forms
from django.core.exceptions import ValidationError
from home.models import SoftwareTraining, SoftwareEngineer


class CreateTrainingForm(forms.Form):
    engineer_id = forms.CharField(label="Engineer ID", required=True)
    engineer_id.widget = engineer_id.hidden_widget()
    software = forms.CharField(label="Software", required=True)

    class Meta:
        model = SoftwareTraining

    def clean(self):
        super(CreateTrainingForm, self).clean()
        software = self.cleaned_data.get('software')
        engineer_id = self.cleaned_data.get('engineer_id')

        if len(software) > 100:
            raise ValidationError("Software is longer than the maximum: 100 characters")
        if len(software) < 2:
            raise ValidationError("Software is shorter than the minimum: 2 characters")
        training = SoftwareTraining.objects.filter(engineer_id_id=engineer_id, software=software)
        if training:
            raise ValidationError(f"This Engineer already has training in {software}")

        return self.cleaned_data
