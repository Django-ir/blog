from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from uuid import uuid4
from .models import Story

UserModel = get_user_model()


class StoriesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create(
            username='testuser',
            email='test@email.com',
            password='passtest'
        )
        cls.story = Story.objects.create(
            user=cls.user,
            content=None
        )

    def test_story_created_as_expected(self):
        now = datetime.now()
        self.assertEqual(type(self.story.id), type(uuid4()))
        self.assertEqual(len(self.story.id.__str__()), len(uuid4().__str__()))
        self.assertEqual(self.story.__str__(), f'Story by {self.user.username}')
        self.assertEqual(self.story.created.time().second, now.time().second)
        self.assertEqual(self.story.like_count, 0)
        self.assertIs(self.story.active, True)
        self.assertIs(self.story.user, self.user)
