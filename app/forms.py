from .models import Project
from django.forms.models import ModelForm


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['engineer']

