# -*- coding: utf-8 -*-

from django.db import models  # noqa: F401
from users.models import CustomUser

class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUSES = (
        ('new', 'New task'),
        ('in_progress', 'In progress'),
        ('testing', 'In testing'),
        ('completed', 'Completed'),
    )

    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
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
    status = models.CharField(max_length=20, choices=STATUSES, default='new')

    def get_tags_list(self):
        tags = []
        for tag in self.tags.all():
            tags.append(tag.name)
        return ', '.join(tags)

    def __str__(self):
        return self.name
