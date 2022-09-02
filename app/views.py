from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectCreateForm, UserUpdateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User
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
        email = request.POST.get('email')
        # username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
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

        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already in use')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
                # return to profile

    context = {}
    return render(request, 'login-signup.html', context)


# ----------------- Engineer's Profile --------------------
def engineer_profile(request, pk):
    engineer = User.objects.get(username=pk)
    my_projects = engineer.project_set.all()

    context = {'engineer': engineer, 'my_projects': my_projects}
    return render(request, 'profile.html', context)


# ----------------- Engineer's Profile Update--------------------
def engineer_profile_update(request):
    user = request.user
    form = UserUpdateForm(instance=user)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.username)

    context = {'form': form}
    return render(request, 'profile-update.html', context)
