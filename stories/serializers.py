from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Story
        fields = ("id", "user", "content", "created", "like_count")
