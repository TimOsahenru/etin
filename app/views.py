from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectCreateForm


# -----------------All Projects--------------------
def projects(request):
    projects = Project.objects.all()

    context = {'projects': projects}
    return render(request, 'index.html', context)


# -----------------Project Detail--------------------
def detail_project(request, pk):
    project = Project.objects.get(name=pk)

    context = {'project': project}
    return render(request, 'project-detail.html', context)


# -----------------Project Create--------------------
def create_project(request):
    page = 'create-page'
    form = ProjectCreateForm()
    user = request.user

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.engineer = user
            project.save()
            return redirect('projects')
            # return to profile

    context = {'form': form, 'page': page}
    return render(request, 'create-update-project.html', context)


# -----------------Project Edit--------------------
def update_project(request, pk):
    project = Project.objects.get(name=pk)
    form = ProjectCreateForm(instance=project)

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
            # Later redirect to profile

    context = {'form': form}
    return render(request, 'create-update-project.html', context)


# -----------------Project Delete--------------------
def delete_project(request, pk):
    project = Project.objects.get(name=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    # Later redirect to profile
    context = {'project': project}

    return render(request, 'project-delete.html', context)