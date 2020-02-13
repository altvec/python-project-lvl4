# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse

from users.models import CustomUser


class Tag(models.Model):
    """Model representing a tag."""

    name_length = 50
    name = models.CharField(max_length=name_length, unique=True)

    def __str__(self):
        """String representation of tag object."""
        return self.name


class TaskStatus(models.Model):
    """Model representing a task status."""

    name_length = 50
    default_state = 'New'
    name = models.CharField(
        max_length=name_length,
        default=default_state,
        unique=True,
    )

    def __str__(self):
        """String representation of task status object."""
        return self.name


class Task(models.Model):
    """Model representing a task."""

    name_length = 128
    description_length = 512

    name = models.CharField(max_length=name_length)
    description = models.TextField(max_length=description_length)
    tags = models.ManyToManyField(Tag, related_name='tasks')
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='tasks_created_by',
    )
    assigned_to = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='tasks_assigned_to',
    )
    status = models.ForeignKey(
        TaskStatus,
        on_delete=models.CASCADE,
        related_name='task_status',
    )

    def __str__(self):
        """String representation of task object."""
        return self.name

    def get_absolute_url(self):
        """Get absolute URL for created task."""
        return reverse('task-detail', kwargs={'pk': self.id})
