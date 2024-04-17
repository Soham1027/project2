from typing import Any, Mapping
from django.contrib import admin
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import (
    UserDatas,
    Players,
    Coaches,
    CourtDetails,
    GroundProviders,
    Profiles,
    Addresses,

)


# Register your models here.


class CoachesAdmin(admin.ModelAdmin):
    list_display = (
    'qualification', 'certificate', 'prices', 'technique', 'specialities', 'experience', 'created_at', 'updated_at',
    'coaches_profile_id')


admin.site.register(Coaches, CoachesAdmin)


class GroundProviderAdmin(admin.ModelAdmin):
    list_display = ('ground_name', 'ammenities', 'facilities', 'created_at', 'updated_at', 'ground_provider_profile_id')


admin.site.register(GroundProviders, GroundProviderAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('aita_ranking', 'skills', 'created_at', 'updated_at', 'player_profile_id')


admin.site.register(Players, PlayerAdmin)


class CourtDetailAdmin(admin.ModelAdmin):
    list_display = (
    'court_name', 'surface_type', 'price', 'created_at', 'updated_at', 'light_availability', 'ground_datas_ids')


admin.site.register(CourtDetails, CourtDetailAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'role', 'created_at', 'updated_at')


admin.site.register(UserDatas, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'nationality', 'user_data_id', 'created_at', 'updated_at')


admin.site.register(Profiles, ProfileAdmin)


class AddressAdmin(admin.ModelAdmin):

    list_display = ('flat_no', 'profile_data_id', 'created_at', 'updated_at')


admin.site.register(Addresses, AddressAdmin)
