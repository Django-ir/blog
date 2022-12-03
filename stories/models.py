
from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.conf import settings
from .managers import StoryManager


class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stories')
    content = models.FileField(upload_to='stories/')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)

    objects = models.Manager()
    actives = StoryManager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Story by {self.user.username}"

    def get_absolute_url(self):
        return reverse("story_detail", kwargs={"id", self.id})


class StoryArchive(models.Model):
    pass
