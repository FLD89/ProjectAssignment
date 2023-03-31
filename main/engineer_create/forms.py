from django import forms
from django.core.exceptions import ValidationError
from home.models import SoftwareEngineer


class CreateEngineerForm(forms.Form):
    engineer_id = forms.CharField(label="Engineer ID", required=True)
    engineer_name = forms.CharField(label="Engineer Name", required=True)

    class Meta:
        model = SoftwareEngineer

    def clean(self):
        super(CreateEngineerForm, self).clean()
        eng_id = self.cleaned_data.get('engineer_id')
        eng_name = self.cleaned_data.get('engineer_name')

        if len(eng_id) > 20:
            raise ValidationError("Engineer ID is longer than the maximum: 20 characters")
        if len(eng_id) < 2:
            raise ValidationError("Engineer ID is shorter than the minimum: 2 characters")
        if len(eng_name) > 100:
            raise ValidationError("Engineer Name is longer than the maximum: 100 characters")
        if len(eng_name) < 5:
            raise ValidationError("Engineer Name is shorter than the minimum: 5 characters")
        engineer = SoftwareEngineer.objects.filter(engineer_id=eng_id)
        if engineer:
            raise ValidationError(f"An Engineer with ID {eng_id} already exists")

        return self.cleaned_data
