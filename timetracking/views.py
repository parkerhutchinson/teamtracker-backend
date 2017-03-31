from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from timetracking.models import *
from timetracking.serializers import TimeTrackingSerializer
from django.http import Http404


class TimeTrackingAPIView(APIView):
    def get_object(self, pk):
        try:
            return TimeTrackers.objects.get(pk=pk)
        except TimeTrackers.DoesNotExist:
            raise Http404

    def get(self, pk):
        timetracker = self.get_object(pk)
        serializer = TimeTrackingSerializer(timetracker)
        return Response(serializer.data)

    def post(self, request):
        serializer = TimeTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        timetracker = self.get_object(pk)
        serializer = TimeTrackingSerializer(timetracker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, pk):
        timetracker = self.get_object(pk)
        timetracker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
