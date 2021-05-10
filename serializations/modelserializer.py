from rest_framework import serializers
from .models import *


class muserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all_ _'