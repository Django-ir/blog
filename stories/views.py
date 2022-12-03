from django.views import generic
from django.contrib.auth import get_user_model
from .models import Story


class StoryListView(generic.ListView):
    model = Story
    template_name = 'stories/story_list.html'

    def get_queryset(self):
        user = self.request.user
        user_test = get_user_model().objects.get(id=2)
        queryset = Story.actives.filter(user__in=[user_test])
        return queryset


class StoryCreateView(generic.CreateView):
    fields = ['content', 'caption']
    template_name = 'stories/story_form.html'
