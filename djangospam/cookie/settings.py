# -*- coding: utf-8 -*-
from django.conf import settings
"""Provides :mod:`djangospam.cookie`specific options:
    
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
"""

try:
    COOKIE_KEY = settings.DJANGOSPAM_COOKIE_KEY
except AttributeError:
    COOKIE_KEY = "dsid"
    
# COOKIE_PASS means we don't know if it is a spammer or not.
try:
    COOKIE_PASS = settings.DJANGOSPAM_COOKIE_PASS
except AttributeError:
    COOKIE_PASS = "0"
try:
    COOKIE_SPAM = settings.DJANGOSPAM_COOKIE_SPAM
except AttributeError:
    COOKIE_SPAM = "1"
    
try:
    COOKIE_LOG = settings.DJANGOSPAM_LOG
except:
    COOKIE_LOG = False