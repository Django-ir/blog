from django.urls import path, include

app_name = 'story'

urlpatterns = [
    # views
    path("story/", include("stories.urls_dir.urls")),
    # api views
    path("api/story/", include("stories.urls_dir.api_urls")),
]
