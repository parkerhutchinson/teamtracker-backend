from rest_framework.serializers import serializers
from timetracking.models import *


class TimeTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTrackers
        fields = ('id', 'name', 'description', 'estimate', 'timer')