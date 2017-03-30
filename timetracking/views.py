from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from timetracking.models import *
from timetracking.serializers import TimeTrackingSerializer
from django.http import Http404


@decorator_method(csrf_exempt)
class TimeTrackingAPI(APIView):
    def get_object(self, pk):
        try:
            return TimeTrackers.objects.get(pk=pk)
        except TimeTrackers.DoesNotExist:
            return Http404

    def get(self):
        timetracker = TimeTracking.get_object(pk)
        serializer = TimeTrackingSerializer(timetracker)
        return Response(serializer.data)

    def post(self, pk):
