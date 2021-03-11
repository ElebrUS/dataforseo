from django.contrib import admin
from . import models


@admin.register(models.Country)
class FieldsCountry(admin.ModelAdmin):
    search_fields = ('code', 'name', 'parent_code', 'iso_code', 'type')
    list_display = ('code', 'name', 'parent_code', 'iso_code', 'type')


@admin.register(models.Location)
class FieldsLocations(admin.ModelAdmin):
    search_fields = ('country', 'code', 'name', 'parent_code', 'type')
    list_display = ('country', 'code', 'name', 'parent_code', 'type')
