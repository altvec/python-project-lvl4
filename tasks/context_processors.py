# -*- coding: utf-8 -*-

from django.conf import settings


def settings_processor(request):
    """Settings processor."""
    return {
        'settings': settings,
    }
