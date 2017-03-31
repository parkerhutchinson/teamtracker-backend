from rest_framework import serializers
from timetracking.models import *


class TimeTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTrackers
        fields = ('id', 'project_name', 'description', 'estimate', 'timer','profile')

        def create(self):
            tracker = validated_data.pop('profile_id')
            profile = validated_data['profile_id']
            TimeTrackers.objects.create(profile=profile, **tracker)