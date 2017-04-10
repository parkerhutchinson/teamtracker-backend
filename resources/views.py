from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from resources.models import *
from resources.serializers import ResourceSerializer
from django.http import Http404


class ResourcesAPIView(APIView):
    def get_object(self, pk):
        try:
            return Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        resource = self.get_object(self, pk)
        serializer = ResourceSerializer(resource, many=True)
        return Response(serializer.data)

    def post(self,  pk):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        resource = self.get_object(self, pk)
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        resource = self.get_object(self, pk)
        serializer = ResourceSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourcesAllAPIView(APIView):
    def get(self, pk):
        resources = Resources.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)