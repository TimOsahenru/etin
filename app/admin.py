from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['engineer', 'name']


admin.site.register(Project, ProjectAdmin)
