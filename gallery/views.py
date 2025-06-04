from rest_framework.generics import ListAPIView
from .models import GalleryImage
from .serializers import GalleryImageSerializer

class GalleryImageListView(ListAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class GalleryImageLimitedListView(ListAPIView):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        return GalleryImage.objects.all()[:4]  # первые 3 фото
