from django.urls import path

# The format_suffix_patterns method will be used to generalize our urls. It will make the urls to work with URIs like http://basic/4 and http://basic/4.json
from rest_framework.urlpatterns import format_suffix_patterns
from .views import API_objects, API_objects_details

urlpatterns = [
    path('basic/', API_objects.as_view()),
    path('basic/<int:pk>/', API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)