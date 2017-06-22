from django.contrib import admin
from resources.models import *


class ResourcesAdmin(admin.ModelAdmin):
    list_display = ['file', 'url', 'name', 'resources_group', 'profile']

    def related_profile(self, obj):
        return obj.profile.first_name

admin.site.register(Resources, ResourcesAdmin)