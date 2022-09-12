from django.shortcuts import render
from rest_framework import generics
from basic_api.models import DRFPost
from .serializers import DRFPostSerializer

# ListCreateAPIView class will be used to provide a list of all model instances. These model instances will be converted to JavaScript objects and transmit to application.
class API_objects(generics.ListCreateAPIView):
    queryset = DRFPost.objects.all()  # queryset attribute is used to provide the model instances to be operated on
    serializer_class = DRFPostSerializer # serializer_class attribute asks for the serializer class to be used to create a JSON model
    

# RetrieveUpdateDestroyAPIView will provide details of an individual object. It  will provide Read, Update and Delete Functions on the model instance.
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
