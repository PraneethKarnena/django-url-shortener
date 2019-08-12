from rest_framework.serializers import ModelSerializer
from . import models


class ServiceSerializer(ModelSerializer):

    class Meta:
        model = models.UrlModel
        fields = '__all__'
