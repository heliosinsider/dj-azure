from django.urls import path
from rest_framework.routers import DefaultRouter

from core.api.v1 import views as viewsets

router = DefaultRouter()

router.register(r'project', viewsets.ProjectViewsets, basename='project')
router.register(r'building', viewsets.BuildingViewSets, basename='building')
 
urlpatterns = [
   
]

urlpatterns += router.urls

