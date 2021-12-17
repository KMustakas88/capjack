from rest_framework import serializers

from .models import Segments

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segments
        fields = '__all__'

    