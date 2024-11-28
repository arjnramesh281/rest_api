from rest_framework import serializers
from .models import *

class sample(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()
    place=serializers.CharField()


class model(serializers.ModelSerializer):
    class Meta:
        model=rest_user
        fields='__all__'