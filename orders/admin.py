from django.contrib import admin
from . import models


@admin.register(models.SearchEngine)
class FieldsOrder(admin.ModelAdmin):
    search_fields = ('name', 'display_name')
    list_display = ('name', 'display_name')


@admin.register(models.Order)
class FieldsOrder(admin.ModelAdmin):
    search_fields = ('id_api', 'user', 'country', 'location', 'engine', 'keyword', 'start', 'end', 'lang', 'status')
    list_display = ('user', 'country', 'location', 'engine', 'keyword', 'start', 'end', 'lang', 'status')


@admin.register(models.DataOrder)
class FieldsDataOrder(admin.ModelAdmin):
    search_fields = ('order', 'type', 'rank_group', 'rank_absolute', 'domain', 'title', 'description', 'url', 'breadcrumb')
    list_display = ('order', 'type', 'rank_group', 'rank_absolute', 'domain', 'title')
