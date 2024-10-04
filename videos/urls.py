from django.urls import path
from videos.views import VideoListView, VideoDetailView

app_name = 'videos'
urlpatterns = [
    path('', VideoListView.as_view(), name='list'),
    path('<int:pk>/', VideoDetailView.as_view(), name='detail'),
]