# -*- coding: utf-8 -*-

from django.test import Client, RequestFactory, TestCase

from tasks.models import Task, TaskStatus
from users.models import CustomUser


class TaskTest(TestCase):
    """Test cases for tasks."""

    def setUp(self):
        """Initial setup before tests."""
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(  # noqa: S106
            username='testuser',
            password='supersecret',
        )
        self.client = Client()

    def create_task(self, name='Test task name'):
        """Create test task."""
        status = TaskStatus.objects.create(name='New')
        return Task.objects.create(
            name=name,
            assigned_to=self.user,
            creator=self.user,
            status=status,
            tags=['important', 'test'],
        )

    def test_task_create(self):
        """Test task creation."""
        task = self.create_task()
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.__str__(), task.name)  # noqa: WPS609
        self.assertEqual(Task.objects.count(), 1)
