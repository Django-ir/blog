from django.urls import path
from stories import apiviews

urlpatterns = [
    path('story/', apiviews.StoryListApiView.as_view(), name='api_list_story'),
    path('story/new/', apiviews.StoryCreateView.as_view(), name='api_create_story'),
    path('story/<uuid:pk>/', apiviews.StoryDetailView.as_view(), name='api_detail_story'),
]
