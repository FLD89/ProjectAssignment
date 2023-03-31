from django import forms
from django.core.exceptions import ValidationError
from home.models import SoftwareEngineer


class UpdateEngineerForm(forms.Form):
    engineer_name = forms.CharField(label="Engineer Name", required=True)

    class Meta:
        model = SoftwareEngineer

    def clean(self):
        super(UpdateEngineerForm, self).clean()
        eng_name = self.cleaned_data.get('engineer_name')

        if len(eng_name) > 100:
            raise ValidationError('Engineer Name is longer than the maximum: 100 characters')
        if len(eng_name) < 5:
            raise ValidationError('Engineer Name is shorter than the minimum: 5 characters')

        return self.cleaned_data
