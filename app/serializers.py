from django.db.models import fields
from django.db.models.base import Model
from .models import UploadImage
from rest_framework import serializers

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=UploadImage
        fields="__all__"
