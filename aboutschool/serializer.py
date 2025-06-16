from rest_framework import serializers
from .models import AboutBlock

class AboutBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutBlock
        fields = ['title', 'content', 'order']
