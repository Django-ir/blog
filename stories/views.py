from django.views import generic
from django.contrib.auth import get_user_model
from .models import Story


class StoryListView(generic.ListView):
    model = Story

    def get_queryset(self):
        user = self.request.user
        user_test = get_user_model().objects.get(id=1)  # temporary test user
        # followings = user.followings.all()
        queryset = Story.actives.filter(user__in=[user_test])
        return queryset


class StoryDetailView(generic.DetailView):
    model = Story


class StoryCreateView(generic.CreateView):
    model = Story
    fields = ['content', 'caption']
