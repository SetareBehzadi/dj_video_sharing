from django.urls import path, include

from apis.views import BookAPIView

urlpatterns = [
    path('', include('videos.urls')),
]