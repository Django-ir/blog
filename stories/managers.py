from django.db.models import Manager


class StoryManager(Manager):
    def get_queryset(self):
        return super(StoryManager, self).get_queryset().filter(active=True)
