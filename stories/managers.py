from django.db.models import Manager
from django.utils import timezone
from datetime import datetime


class StoryManager(Manager):
    def get_queryset(self):
        timestamp_now = datetime.now().timestamp()
        one_day_in_seconds = 86400
        time_of_24_hours_ago_in_seconds = timestamp_now - one_day_in_seconds
        datetime_of_yesterday = datetime.utcfromtimestamp(time_of_24_hours_ago_in_seconds).replace(tzinfo=timezone.utc)
        return super(StoryManager, self).get_queryset().filter(created__gt=datetime_of_yesterday)
