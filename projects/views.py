from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.object.all()
    context = {
        'project': projects
    }
    return render(request.'project_index.html',
                  context)
