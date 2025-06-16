from rest_framework import serializers
from .models import Banner
//serializaer
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
