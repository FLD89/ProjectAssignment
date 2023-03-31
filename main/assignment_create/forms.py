from django import forms
from django.core.exceptions import ValidationError
from home.models import ProjectEngineerLookup, SoftwareEngineer, SoftwareTraining, Project


class CreateAssignmentForm(forms.Form):
    project_id = forms.CharField()
    project_id.widget = project_id.hidden_widget()
    engineer_id = forms.CharField(label="Engineer ID", required=True)

    class Meta:
        model = ProjectEngineerLookup

    def clean(self):
        super(CreateAssignmentForm, self).clean()
        project_id = self.cleaned_data.get('project_id')
        engineer_id = self.cleaned_data.get('engineer_id')

        engineer = SoftwareEngineer.objects.filter(engineer_id=engineer_id)
        if not engineer:
            raise ValidationError("This Engineer ID does not exist")

        project = Project.objects.filter(project_id=project_id)
        if not project:
            raise ValidationError("This Project ID does not exist")

        project = Project.objects.get(project_id=project_id)
        project_software = str(project.software)
        # new variable engineer_training gets training record with matching engineer_id and software, only if one exists
        engineer_training = SoftwareTraining.objects.filter(engineer_id_id=engineer_id, software=project_software)
        if not engineer_training:
            raise ValidationError(f"Engineer {engineer_id} does not have training in {project_software}")

        assignment = ProjectEngineerLookup.objects.filter(engineer_id_id=engineer_id, project_id_id=project_id)
        if assignment:
            raise ValidationError(f"Engineer {engineer_id} is already assigned to this project")

        return self.cleaned_data
