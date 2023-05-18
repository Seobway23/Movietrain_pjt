from rest_framework import serializers
from .models import User


class MovieListSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = User
        fields = "__all__"
        # fields = ('원하는 필드')
