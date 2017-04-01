from rest_framework import serializers
from resources.models import *


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        models = Resources
        fields = ('id', 'filename', 'file', 'resources_group', 'profile')
