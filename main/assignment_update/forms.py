from django import forms
from django.core.exceptions import ValidationError
from home.models import ProjectEngineerLookup, Project, SoftwareEngineer, SoftwareTraining


class UpdateAssignmentForm(forms.Form):
    engineer_id = forms.CharField(label="Engineer ID", required=True)
    project_id = forms.CharField(label="Project ID", required=True)

    class Meta:
        model = ProjectEngineerLookup

    def clean(self):
        super(UpdateAssignmentForm, self).clean()
        engineer_id = self.cleaned_data.get('engineer_id')
        project_id = self.cleaned_data.get('project_id')

        if len(engineer_id) > 20:
            raise ValidationError("Engineer ID is longer than the maximum: 20 characters")
        if len(engineer_id) < 2:
            raise ValidationError("Engineer ID is shorter than the minimum: 2 characters")

        project = Project.objects.filter(project_id=project_id)
        if not project:
            raise ValidationError("This Project ID does not exist")

        engineer = SoftwareEngineer.objects.filter(engineer_id=engineer_id)
        if not engineer:
            raise ValidationError("This Engineer ID does not exist")

        # Confirms assignment of same engineer_id and project_id does not exist already
        assignment = ProjectEngineerLookup.objects.filter(engineer_id_id=engineer_id, project_id_id=project_id)
        if assignment:
            raise ValidationError(f"This Engineer {engineer_id} is already assigned to project {project_id}")

        # Confirms software_training for that engineer_id and project software exists
        project = Project.objects.get(project_id=project_id)
        engineer_training = SoftwareTraining.objects.filter(engineer_id_id=engineer_id, software=project.software)
        if not engineer_training:
            raise ValidationError(f"Engineer {engineer_id} does not have the required training in {project.software}")

        return self.cleaned_data
