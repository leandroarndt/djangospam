# -*- coding: utf-8 -*-
"""Offers spamform_ tag and SpamCookieMiddleware_ for prohibiting site
access to known spam bots. You should add
`djangospam.cookie.SpamCookieMiddleware` to your
`MIDDLEWARE_CLASSES` at `settings.py` **and** use spamform_ tag before your
true form. You must also add the following to your urls.py::
    
    ...    
    
    import djangospam.cookie

    urlpatterns = patterns(
        ...
        r"^somewhere/", include(djangospam.cookie.urls),
        ...
        )

In your template, you must add the following **before** the real form::
    
    {% include 'djangospam/cookieform.html' }

If you want set a different cookie key or different values, use
the following variables on your settings file::
    
    DJANGOSPAM_COOKIE_NAME = "MyAlternativeCookieKey" # Default: "dsid"
    DJANGOSPAM_COOKIE_PASS = "AnotherOkValue"         # Default: "1"
    DJANGOSPAM_COOKIE_SPAM = "AnotherSpamValue"       # Default: "0"

You can also activate logging:
    
    DJANGOSPAM_LOG = "/path/to/log.file" # Default: False
"""

from django.conf import settings

# We want to make it available at djangospam.cookie.SpamCookieMiddleware
from middleware import SpamCookieMiddleware

try:
    COOKIE_KEY = settings.DJANGOSPAM_COOKIE_KEY
except NameError:
    COOKIE_KEY = "dsid"
    
# COOKIE_PASS means we don't know if it is a spammer or not.
try:
    COOKIE_PASS = settings.DJANGOSPAM_COOKIE_PASS
except NameError:
    COOKIE_PASS = "0"
try:
    COOKIE_SPAM = settings.DJANGOSPAM_COOKIE_SPAM
except NameError:
    COOKIE_SPAM = "1"
    
try:
    COOKIE_LOG = settings.DJANGOSPAM_LOG
except:
    COOKIE_LOG = False