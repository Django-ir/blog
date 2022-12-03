from django.urls import path
from .import views

app_name = 'story'

urlpatterns = [
    path('story/', views.StoryListView.as_view(), name='list_story'),
]