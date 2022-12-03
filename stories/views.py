from django.shortcuts import render
from django.views import generic


class StoryListView(generic.ListView):
    model = Story
    template_name = 'stories/story_list.html'


class StoryCreateView(generic.CreateView):
    fields = ['content', 'caption']
    template_name = 'stories/story_form.html'


