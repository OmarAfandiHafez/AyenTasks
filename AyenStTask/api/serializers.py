from rest_framework import serializers
from .models import MetaData, Document


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = ('pk', 'name', 'string')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('pk', 'name', 'file')
