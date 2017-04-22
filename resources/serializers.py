from rest_framework import serializers
from resources.models import *


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ('id', 'name', 'file', 'resources_group', 'profile')
