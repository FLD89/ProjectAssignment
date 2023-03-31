from django import forms
from django.core.exceptions import ValidationError
from home.models import Project, SoftwareTraining, ProjectEngineerLookup


class UpdateProjectForm(forms.Form):
    project_name = forms.CharField(label="Project Name", required=True)
    software = forms.CharField(label="Software", required=True)
    project_id = forms.CharField()
    project_id.widget = software.hidden_widget()

    class Meta:
        model = Project

    def clean(self):
        super(UpdateProjectForm, self).clean()
        project_name = self.cleaned_data.get('project_name')
        software = self.cleaned_data.get('software')
        project_id = self.cleaned_data.get('project_id')

        if project_name:
            if len(project_name) > 100:
                raise ValidationError("Project Name is longer than the maximum: 100 characters")
            if len(project_name) < 5:
                raise ValidationError("Project Name is shorter than the minimum: 5 characters")

        if software:
            if len(software) > 100:
                raise ValidationError("Software is longer than the maximum: 100 characters")
            if len(software) < 2:
                raise ValidationError("Software is shorter than the minimum: 2 characters")

        project = Project.objects.get(project_id=project_id)
        lookups = ProjectEngineerLookup.objects.all()
        # Iterates through existing Assignments to see if assigned Engineer(s) do not have training in software being updated to
        for lookup in lookups:
            if lookup.project_id_id == project.project_id:
                engineer_training = SoftwareTraining.objects.filter(engineer_id_id=lookup.engineer_id_id, software=software)
                if not engineer_training:
                    raise ValidationError(
                        f"Engineer {lookup.engineer_id_id} is already assigned to this project and does not have training in {software}")

        return self.cleaned_data
