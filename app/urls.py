from django.contrib.auth.urls import path
from . import views
from .views import DetailProject


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project-detail/<str:pk>/', DetailProject.as_view(), name='project-detail'),
    # path('project-detail/<str:pk>/', views.detail_project, name='project-detail'),
    path('create-project/', views.create_project, name='create-project'),
    path('update-project/<str:pk>/', views.update_project, name='update-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),

    path('profile/<str:pk>/', views.engineer_profile, name='profile'),
    path('update-profile/', views.engineer_profile_update, name='update-profile'),

]
