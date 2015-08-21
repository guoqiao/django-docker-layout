from django.contrib import admin
from . import models as m


@admin.register(m.Facebook)
class BlogAdmin(admin.ModelAdmin):
    search_fileds = ['title', 'slug']
    list_display = ['title', 'user']
