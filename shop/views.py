from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Part
from shop.serializers import PartSerializer


class ListPart(APIView):
    def get(self, request, format=None):
        parts = Part.objects.all()
        serializer = PartSerializer(parts, many=True)
        return JsonResponse(serializer.data, safe=False)
