from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    git_hub_link = models.URLField(max_length=2000, null=True, blank=True)
    live_link = models.URLField(max_length=2000, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    tech_used = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.engineer.username

    class Meta:
        ordering = ['-created_at']

