from django.contrib import admin
from .models import Project, User, Expertise


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['engineer', 'name']


admin.site.register(User)
admin.site.register(Expertise)
admin.site.register(Project, ProjectAdmin)
