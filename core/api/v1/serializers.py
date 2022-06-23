from core.models import Building, Project
from rest_framework import serializers
from django.db import transaction


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields =  '__all__'
        exclude = ('building_id', 'organization_id', 'project_administrator_id', 'company_id',)


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        # fields = '__all__'
        exclude = ('organization_id',)