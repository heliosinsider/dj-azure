from django.urls import path
from rest_framework.routers import DefaultRouter

# app_name = "example"
router = DefaultRouter()

# router.register(r'example', viewsets.ExampleViewSets, basename='example')
 
urlpatterns = [
   
]

urlpatterns += router.urls

