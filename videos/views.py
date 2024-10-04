from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics

from videos.models import Video
from videos.serializers import VideoSerializer


class VideoListView(generics.ListAPIView):
    print("sss"*20)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    print(serializer_class)

class VideoDetailView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer