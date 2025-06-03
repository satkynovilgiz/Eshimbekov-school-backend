from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerSerializer

class BannerView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
