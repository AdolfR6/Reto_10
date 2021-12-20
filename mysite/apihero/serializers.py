from rest_framework import serializers
from .models import Hero

class HeroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields =('id','name','alias')