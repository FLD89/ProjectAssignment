from django import forms
from django.core.exceptions import ValidationError
from home.models import SoftwareTraining, SoftwareEngineer, ProjectEngineerLookup, Project


class UpdateTrainingForm(forms.Form):
    engineer_id = forms.CharField(label="Engineer ID", required=True)
    software = forms.CharField(label="Software", required=True)
    training_id = forms.CharField()
    training_id.widget = software.hidden_widget()

    class Meta:
        model = SoftwareTraining

    def clean(self):
        super(UpdateTrainingForm, self).clean()
        engineer_id = self.cleaned_data.get('engineer_id')
        software = self.cleaned_data.get('software')
        training_id = self.cleaned_data.get('training_id')

        if len(software) > 100:
            raise ValidationError("Software is longer than the maximum: 100 characters")
        if len(software) < 2:
            raise ValidationError("Software is shorter than the minimum: 2 characters")

        engineer = SoftwareEngineer.objects.filter(engineer_id=engineer_id)
        if not engineer:
            raise ValidationError("This Engineer ID does not exist")

        engineer_training = SoftwareTraining.objects.filter(engineer_id_id=engineer_id, software=software)
        if engineer_training:
            raise ValidationError(f"Engineer {engineer_id} already has training in {software}")

        if training_id:
            training = SoftwareTraining.objects.get(training_id=training_id)
            assignments = ProjectEngineerLookup.objects.all()
            # Iterates through all assignments to see if training software corresponds to software required for assigned project
            for assignment in assignments:
                if assignment.engineer_id_id == engineer_id:
                    project = Project.objects.get(project_id=assignment.project_id_id)
                    if project.software == training.software:
                        raise ValidationError(f"Engineer {engineer_id} requires Training in {training.software} for assigned Project {project.project_name}")

        return self.cleaned_data
