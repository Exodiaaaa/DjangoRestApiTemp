
from rest_framework import serializers, viewsets
from MyApp.models import Dht

class DhtSerialize(serializers.ModelSerializer):
    class Meta :
        model = Dht
        fields = ['id', 'temp','hum','dt']