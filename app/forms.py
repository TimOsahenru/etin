from .models import Project, User
from django.forms.models import ModelForm


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['engineer']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['mobile_number', 'location', 'years_of_experience', 'tech_stack', 'about_me', 'avatar']
