from django.urls import path

from playlist.views import PlayListView
from videos.views import VideoListView, VideoDetailView

app_name = 'videos'
urlpatterns = [
    path('', PlayListView.as_view(), name='list'),
    path('<int:pk>/', VideoDetailView.as_view(), name='detail'),
]