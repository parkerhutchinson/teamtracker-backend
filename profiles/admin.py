from django.contrib import admin
from profiles.models import *


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',  'title',
                    'department', 'team_group', )

    fields = ('first_name', 'last_name', 'email', 'profile_image_inline', 'profile_image', 'title',
              'department', 'team_group', 'bio', 'twitter_handle',
              'overwatch_handle', 'instagram_handle', 'pinterest_handle',
              'steam_handle', )

    readonly_fields = ('profile_image_inline',)


admin.site.register(Profiles, ProfilesAdmin)