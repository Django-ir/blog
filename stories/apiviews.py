from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import Story
from .serializers import StorySerializer


class StoryListApiView(ListAPIView):
    queryset = Story.actives.all()
    serializer_class = StorySerializer


class StoryDetailView(RetrieveAPIView):
    queryset = Story.actives.all()
    serializer_class = StorySerializer


class StoryCreateView(CreateAPIView):
    queryset = Story.actives.all()
    serializer_class = StorySerializer
