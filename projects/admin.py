from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'technology']
    list_filter = ['technology']
    #list_editable = ['description', 'technology']
    #prepopulated_fields = {'technology': ('title',)}


admin.site.register(Project, ProjectAdmin)
