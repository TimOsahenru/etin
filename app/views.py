from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectCreateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
@login_required(login_url='login')
def create_project(request):
    page = 'create-page'
    form = ProjectCreateForm()
    user = request.user

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.engineer = user
            project.save()
            return redirect('projects')
            # return to profile

    context = {'form': form, 'page': page}
    return render(request, 'create-update-project.html', context)


# -----------------Project Edit--------------------
@login_required(login_url='login')
def update_project(request, pk):
    project = Project.objects.get(name=pk)
    form = ProjectCreateForm(instance=project)

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
            # Later redirect to profile

    context = {'form': form}
    return render(request, 'create-update-project.html', context)


# -----------------Project Delete--------------------
@login_required(login_url='login')
def delete_project(request, pk):
    project = Project.objects.get(name=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    # Later redirect to profile
    context = {'project': project}

    return render(request, 'project-delete.html', context)


# ----------------- Login --------------------
def login_user(request):

    if request.user.is_authenticated:
        return redirect('projects')

    page = 'login-page'

    if request.method == 'POST':
        # email =
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'Email or Password does not exist')

    context = {'page': page}
    return render(request, 'login-signup.html', context)


# ----------------- Logout --------------------
def logout_user(request):
    logout(request)
    # later redirect to profile
    return redirect('login')


# ----------------- SignUp --------------------
def signup_user(request):

    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        # email =
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
                # return to profile

    context = {}
    return render(request, 'login-signup.html', context)
