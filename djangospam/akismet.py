# -*- coding: utf-8 -*-
"""Defines a comment checker that should be attached to your commented model.
Eg.:
    
    from djangospam import akismet
    
    class MyModel(...):
        ...
    
    try:
        akismet.register(MyModel)
    except akismet.AlreadyModerated:
        pass
"""
from __future__ import unicode_literals
from django.contrib.comments.moderation import CommentModerator, \
                                               moderator, AlreadyModerated
from django.conf import settings
from urllib import urlencode
import httplib
import djangospam

AKISMET_URL = ".".join([settings.AKISMET_KEY, "rest.akismet.com"])
AKISMET_PORT = 80
AKISMET_PATH = "/1.1/comment-check"
AKISMET_USERAGENT = "%s/%s | %s/%s" % (settings.AKISMET_USERAGENT,
                                       settings.AKISMET_USERAGENT_VERSION,
                                       "djangospam", djangospam.version)

def register(model):
    """Just a wrapper around django.contrib.comments.moderation.register.
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
django.contrib.comments.moderation."""

    def allow(self, comment, content_object, request):
        """Moderates comments."""
        POST = urlencode({"blog": settings.AKISMET_BLOG,
                "user_ip": comment.ip_address,
                "user_agent": request.META['HTTP_USER_AGENT'],
                "referrer": request.META['HTTP_REFERRER'],
                "comment_author": comment.user_name,
                "comment_author_email": comment.user_email,
                "comment_author_url": comment.user_url,
                "comment_content": comment.comment})
        connection = httplib.HTTPConnection(AKISMET_URL, AKISMET_PORT)
        connection.request("POST", AKISMET_PATH, POST,
                           {"User-Agent": AKISMET_USERAGENT,
                            "Content-type":"application/x-www-form-urlencoded"
                            })
        response = connection.getresponse()
        if response.read() == "false":
            return True
        elif response.read() == "true" and settings.DISCARD_SPAM:
            return False
        elif response.read() == "true":
            comment.is_removed = True
            comment.is_public = False
            return True
        else:
            raise AkismetError(response.status, response.read())
