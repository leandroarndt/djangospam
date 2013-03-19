# -*- coding: utf-8 -*-
"""Defines a cookie-based comment moderator that should be attached to
your commented model. This moderator tests comment post requests for
the djangospam cookie and discards those which don't have it.
See :mod:`djangospam.cookie.middleware` for mor info on the cookie system.
Code that uses this comment moderator **must** use that middleware.

Eg.::
    
    from djangospam.cookie import moderator as cookie
    
    class MyModel(...):
        ...
    
    try:
        cookie.register(MyModel)
    except cookie.AlreadyModerated:
        pass

See :mod:`djangospam.settings` for available options.
"""
from __future__ import unicode_literals

from django.contrib.comments.moderation import CommentModerator, \
                                               moderator, AlreadyModerated

from djangospam import settings

def register(model):
    """Just a wrapper around django.contrib.comments.moderation.register.
It's only argument is the model for comment moderation."""
    moderator.register(model, CookieModerator)

class CookieModerator(CommentModerator):
    """The comment moderator, defined according to the needs of
django.contrib.comments.moderation."""
    
    def allow(self, comment, content_object, request):
        """Tests comment post requests for the djangospam cookie."""
        # Tests for cookie:
        if settings.COOKIE_KEY not in request.COOKIES \
            and settings.DISCARD_SPAM:
                return False
        elif settings.COOKIE_KEY not in request.COOKIES:
            comment.is_removed = True
            comment.is_public = False
            return True

