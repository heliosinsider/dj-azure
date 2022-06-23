from core.models import Building, Project
from rest_framework import serializers
from django.db import transaction


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =  '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'