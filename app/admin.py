from django.contrib import admin
from .models import Project, User


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['engineer', 'name']


admin.site.register(User)
admin.site.register(Project, ProjectAdmin)
