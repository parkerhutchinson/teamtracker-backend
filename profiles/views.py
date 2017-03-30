from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles.models import *
from profiles.serializers import ProfilesSerializer


class ProfilesAPIView(APIView):
    def get(self, request, format=None):
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(serializer.data)