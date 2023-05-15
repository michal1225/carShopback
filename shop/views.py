import django_filters
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Part
from shop.serializers import PartSerializer


class ListPart(ListAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

