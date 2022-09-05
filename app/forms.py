from .models import Project, User
from django.forms.models import ModelForm
from django import forms


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['engineer']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project name'}),
            'git_hub_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link to github repo'}),
            'live_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link to live project'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'tech_used': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stack1 | Stack2 | Stack3'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mobile_number', 'expertise', 'location', 'years_of_experience', 'tech_stack', 'about_me', 'avatar']
        widgets = {
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number', 'data-msg': 'Phone number required'}),
            'expertise': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country | State',  'data-msg': 'Location required'}),
            'years_of_experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Years of experience'}),
            'tech_stack': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stack1 | Stack2 | Stack3'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'})
        }
