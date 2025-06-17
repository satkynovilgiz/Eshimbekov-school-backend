from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer

class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all().order_by('-created_at')
    serializer_class = VideoSerializer
