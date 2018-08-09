from rest_framework import serializers
from WebAnalyzer.models import *


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResultModel
        fields = ('layer', 'feature')
        read_only_fields = ('layer', 'feature')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    result = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = ImageModel
        fields = ('image', 'token', 'uploaded_date', 'updated_date', 'result')
        read_only_fields = ('token', 'uploaded_date', 'updated_date', 'result')
