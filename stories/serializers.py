from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Story
        fields = ("id", "user", "content", "active", "created", "like_count")
