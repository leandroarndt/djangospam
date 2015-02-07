# -*- coding: utf-8 -*-
"""Defines an Akismet-based comment moderator that should be attached to
your commented model.
Eg.::
    
    from djangospam.akismet import moderator as akismet
    
    class MyModel(...):
        ...
    
    try:
        akismet.register(MyModel)
    except akismet.AlreadyModerated:
        pass

.. warning::
    Since version 0.4.0, the Akismet moderator has been turned a separate
    subpackage. Code using it must be rewritten as follows::
        
        from djangospam import akismet
        
    must be changed to::
        
        from djangospam.akismet import moderator as akismet
    
    Using from `djangospam import akismet` is now deprecated and won't be
    available from 1.0.0 on.

Settings
++++++++

The following settings are mandatory:

AKISMET_BLOG
    Your home page URL, including http://
AKISMET_KEY
    Your application key at akismet.com
AKISMET_USERAGENT
    Your application name
AKISMET_USERAGENT_VERSION
    Your application version

This setting is optional:
    
DISCARD_SPAM
    If spam should be either automaticaly discarded or marked as not public and
    removed. Defaults to `False`.
"""
from __future__ import unicode_literals

try:
    from django_comments.moderation import CommentModerator, \
                                            moderator, AlreadyModerated
except ImportError:
    from django.contrib.comments.moderation import CommentModerator, \
                                               moderator, AlreadyModerated

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection

import djangospam
from djangospam import settings

AKISMET_URL = ".".join([settings.AKISMET_KEY, "rest.akismet.com"])
AKISMET_PORT = 80
AKISMET_PATH = "/1.1/comment-check"
AKISMET_USERAGENT = "%s/%s | %s/%s" % \
                    (settings.AKISMET_USERAGENT,
                     settings.AKISMET_USERAGENT_VERSION,
                     "djangospam", djangospam.__version__)

def register(model):
    """Just a wrapper around django_comments.moderation.register.
It's only argument is the model for comment moderation."""
    moderator.register(model, Akismet)
    
class AkismetError(Exception):
    """Throwed if reponse is unknown. Prints HTTP status and response text."""
    def __init__(self, status, text):
        self.status, self.text = status, text
    
    def __str__(self):
        return "%s %s" % (self.status, self.text)
        
class Akismet(CommentModerator):
    """The comment moderator, defined according to the needs of
django_comments.moderation."""

    def allow(self, comment, content_object, request):
        """Moderates comments."""
        
        POST = urlencode({
                "blog": settings.AKISMET_BLOG.encode("utf-8"),
                "user_ip": comment.ip_address,
                "user_agent": request.META.get('HTTP_USER_AGENT', "").
                                                encode("utf-8"),
                "referrer": request.META.get('HTTP_REFERRER', "").
                                                encode("utf-8"),
                "comment_author": comment.user_name.encode("utf-8"),
                "comment_author_email": comment.user_email.encode("utf-8"),
                "comment_author_url": comment.user_url.encode("utf-8"),
                "comment_content": comment.comment.encode("utf-8")})
        connection = HTTPConnection(AKISMET_URL, AKISMET_PORT)
        connection.request("POST", AKISMET_PATH, POST,
                           {"User-Agent": AKISMET_USERAGENT,
                            "Content-type":"application/x-www-form-urlencoded"
                            })
        response = connection.getresponse()
        status, result = response.status, response.read()
        if result == "false":
            return True
        elif result == "true" and settings.DISCARD_SPAM:
            return False
        elif result == "true":
            comment.is_removed = True
            comment.is_public = False
            return True
        else:
            raise AkismetError(status, result)
