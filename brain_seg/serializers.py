from rest_framework import serializers
from .models import UploadImage


class UploadImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UploadImage
        fields = '__all__'
