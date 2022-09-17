import django_filters
from .models import *


class EngineerFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['expertise']
