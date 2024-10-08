from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics, status
from rest_framework.response import Response

from videos.models import Video
from videos.serializers import VideoSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    #return Response(serializer_class.data, status = status.Htt_200_OK)

class VideoDetailView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer