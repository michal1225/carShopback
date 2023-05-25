import django_filters
from django.http import Http404
from django.utils import timezone
from django.views.generic import DetailView, DeleteView
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Part
from shop.serializers import PartSerializer


class PartsViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]

class ListPart(APIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

    def get(self, request):
        filtered_parts = Part.objects.filter(name__icontains=self.request.GET.get('name'))
        serializer = PartSerializer(filtered_parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        filtered_parts = Part.objects.filter(name__icontains=self.request.GET.get('name'))
        return filtered_parts


class PartDetailView(APIView):
    model = Part

    def get_object(self, pk):
        try:
            return Part.objects.get(pk=pk)
        except Part.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




