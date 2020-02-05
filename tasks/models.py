# -*- coding: utf-8 -*-

from django.db import models  # noqa: F401

from users.models import CustomUser


class Tag(models.Model):
    """Model representing a tag."""

    name_length = 128
    name = models.CharField(max_length=name_length, unique=True)

    def __str__(self):
        """String representation of tag object."""
        return self.name


class Task(models.Model):
    """Model representing a task."""

    name_length = 128
    description_length = 512
    status_length = 20
    statuses = (
        ('new', 'New task'),
        ('in_progress', 'In progress'),
        ('testing', 'In testing'),
        ('completed', 'Completed'),
    )

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
    status = models.CharField(
        max_length=status_length,
        choices=statuses,
        default='new',
    )

    def get_tags_list(self):
        """Get tags list for a task."""
        tags = []
        for tag in self.tags.all():
            tags.append(tag.name)
        return ', '.join(tags)

    def __str__(self):
        """String representation of task object."""
        return self.name
