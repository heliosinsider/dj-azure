from core.api.v1.serializers import BuildingSerializer, ProjectSerializer
from core.models import Building, Project
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.conf import settings

from rest_framework.permissions import AllowAny, IsAuthenticated
import django_filters
from django_filters import rest_framework as filters


class ProjectViewsets(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class BuildingViewSets(viewsets.ModelViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()