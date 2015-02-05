# -*- coding: utf-8 -*-
""".. versionadded:: 0.3.0

The cookie middleware uses cookies to identify known spam bots. Simple
crawlers usually don't accept cookies, but spam bots may accept, since
a website may require this to receive comments. In order to use the
cookie middleware, add `djangospam.cookie.middleware.SpamCookieMiddleware`
to `MIDDLEWARE_CLASSES` at your settins file (usually `settings.py`).
In your template, insert::
    
    {% include 'djangospam/cookieform.html' %}

You must also add `(r"^somewhere/", include("djangospam.cookie.urls")`
to your url patterns (usually in your root urls.conf; `somewhere`
may be any path).

You may also define some variables at your settings file to customize
your cookie:

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
    
Comment moderator
+++++++++++++++++

.. versionadded:: 0.4.0

This package also defines a comment moderator which disallows posts
without the djangospam cookie. See :mod:`djangospam.cookie.moderator` below
for more info.
"""

# We want to make it available at djangospam.cookie.SpamCookieMiddleware
from djangospam.cookie.middleware import SpamCookieMiddleware
