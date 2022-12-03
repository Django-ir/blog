from django.contrib import admin
from .models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'created']
    date_hierarchy = 'created'
    ordering = ['-created']


admin.site.register(Story, StoryAdmin)
