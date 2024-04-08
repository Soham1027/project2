from django.contrib import admin
from typing import Any, Mapping

from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import (
      ProfileAvailabilities,
      CourtAvailabilities,
     
)
# Register your models here.

admin.site.register(ProfileAvailabilities)
admin.site.register(CourtAvailabilities)
