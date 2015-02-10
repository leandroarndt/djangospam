# -*- coding: utf-8 -*-
"""
.. versionadded:: 0.4.0

Defines a cookie-based comment moderator that should be attached to
your commented model. This moderator tests comment post requests for
the djangospam cookie and discards those which don't have it.
See :mod:`djangospam.cookie.middleware` for more info on the cookie system.
Code that uses this comment moderator **must** use that middleware.

Your models file should be like this::
    
    from djangospam.cookie import moderator as cookie
    
    class MyModel(...):
        ...
    
    try:
        cookie.register(MyModel)
    except cookie.AlreadyModerated:
        pass

Settings
++++++++

The following settings are optional:

DJANGOSPAM_COOKIE_KEY
    The cookie identifier. Defaults to `dsid`.
DJANGOSPAM_COOKIE_PASS
    The initial value of the cookie. It is used only to know beforehand if
    the user agent accepts cookies. Defaults to `0`.
DJANGOSPAM_COOKIE_SPAM
    The cookie value for known spammers. If the HTTP request presents
    djangospam cookie with this value, the middleware will return a 404
    status code (moved permanently or forbidden, according to the standards).
    Defaults to `1`.
DJANGOSPAM_DISCARD_NO_COOKIE
    If the comment should be discarded case the cookie is not present.
    That will happen if either this option or `DISCARD_SPAM` is set to `True`.
    Defaults to `False`.
DISCARD_SPAM
    If spam should be either automaticaly discarded or marked as not public and
    removed. See `DJANGOSPAM_DISCARD_NO_COOKIE`. Defaults to `False`.
"""
from __future__ import unicode_literals

try:
    from django_comments.moderation import CommentModerator, \
                                            moderator, AlreadyModerated
except ImportError:
    from django.contrib.comments.moderation import CommentModerator, \
                                               moderator, AlreadyModerated
                                        
from djangospam import settings

def register(model):
    """Just a wrapper around django_comments.moderation.register.
It's only argument is the model for comment moderation."""
    moderator.register(model, CookieModerator)

class CookieModerator(CommentModerator):
    """The comment moderator, defined according to the needs of
django_comments.moderation."""
    
    def allow(self, comment, content_object, request):
        """Tests comment post requests for the djangospam cookie."""
        # Tests for cookie:
        if settings.COOKIE_KEY not in request.COOKIES \
            and (settings.DISCARD_SPAM or settings.DISCARD_NO_COOKIE):
                return False
        elif settings.COOKIE_KEY not in request.COOKIES:
            comment.is_removed = True
            comment.is_public = False
            return True
        return True
