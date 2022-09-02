from django.db import models
from django.contrib.auth.models import AbstractUser


class SocialMediaHandle:
    pass
    # user =
    # name =
    # icon =
    # url =


class User(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200, default='Country | State')
    years_of_experience = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(default='avatar.svg')
    tech_stack = models.CharField(max_length=500, default='Stack1 | Stack2 | Stack3')
    about_me = models.TextField(null=True, blank=True)
    # social_media_handle =

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Project(models.Model):

    engineer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    git_hub_link = models.URLField(max_length=2000, null=True, blank=True)
    live_link = models.URLField(max_length=2000, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    tech_used = models.CharField(max_length=100, default='Stack1 | stack2')
    image = models.ImageField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.engineer.username

    class Meta:
        ordering = ['-created_at']

