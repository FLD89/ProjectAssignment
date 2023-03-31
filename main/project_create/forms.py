from django import forms
from django.core.exceptions import ValidationError
from home.models import Project


class CreateProjectForm(forms.Form):
    project_name = forms.CharField(label="Project Name", required=True)
    software = forms.CharField(label="Software", required=True)

    class Meta:
        model = Project

    def clean(self):
        super(CreateProjectForm, self).clean()
        project_name = self.cleaned_data.get('project_name')
        software = self.cleaned_data.get('software')

        if len(project_name) > 100:
            raise ValidationError("Project Name is longer than the maximum: 100 characters")
        if len(project_name) < 5:
            raise ValidationError("Project Name is shorter than the minimum: 5 characters")

        if len(software) > 100:
            raise ValidationError("Software is longer than the maximum: 100 characters")
        if len(software) < 2:
            raise ValidationError("Software is shorter than the minimum: 2 characters")

        project = Project.objects.filter(project_name=project_name)
        if project:
            raise ValidationError("There is another Project with that name")

        return self.cleaned_data
