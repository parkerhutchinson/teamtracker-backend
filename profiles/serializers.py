from validate_email import validate_email
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from rest_framework import serializers
from profiles.models import *
#


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('id', 'first_name', 'last_name',
                  'email', 'profile_image', 'bio',
                  'department', 'title', 'team_group',
                  'twitter_handle', 'overwatch_handle',
                  'instagram_handle', 'pinterest_handle',
                  'steam_handle')

    # def validate_email(self, value):
    #     valid_email = validate_email(value)
    #     if not valid_email:
    #         raise ValidationError(_("The email entered is not a valid format for email address."))
