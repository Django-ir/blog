from django.urls import path
from stories import views

urlpatterns = [
    path('', views.StoryListView.as_view(), name='list_story'),
    path('new/', views.StoryCreateView.as_view(), name='create_story'),
    path('<uuid:pk>/', views.StoryDetailView.as_view(), name='detail_story'),
]