# -*- coding: utf-8 -*-
"""Provides a common configuration interface for all :mod:`djangospam`
modules. These options should be set at `settings.py`.

General options
+++++++++++++++

This option is used by more than one djangospam module/package:

DISCARD_SPAM
    If spam should be either automaticaly discarded or marked as not public and
    removed. Defaults to `False`.

Logging settings
++++++++++++++++

These afect :mod:`djangospam.logger`:

DJANGOSPAM__LOG
    Log file path and name. Defaults to `False` (no logging).
DJANGOSPAM_FAIL_ON_LOG
    If djangospam should raise an exception when it fails to log. Defaults
    to `False`.

Cookie settings
+++++++++++++++

The following settings are optional and used by :mod:`djangospam.cookie`:

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
    Defaults to `False`. Used by :mod:`djangospam.cookie.moderator`.
    
Akismet settings
++++++++++++++++

You **must** define the variables below at `settings.py` if you want to
use :mod:`djangospam.akismet`:

AKISMET_BLOG
    Your home page URL, including http://
AKISMET_KEY
    Your application key at akismet.com
AKISMET_USERAGENT
    Your application name
AKISMET_USERAGENT_VERSION
    Your application version
"""
from django.conf import settings

# Optional settings:
try:
    DISCARD_SPAM = settings.DISCARD_SPAM
except AttributeError:
    DISCARD_SPAM = False

try:
    DJANGOSPAM_LOG = settings.DJANGOSPAM_LOG
except:
    DJANGOSPAM_LOG = False

try:
    DJANGOSPAM_FAIL_ON_LOG = settings.DJANGOSPAM_FAIL_ON_LOG
except AttributeError:
    DJANGOSPAM_FAIL_ON_LOG = False

try:
    COOKIE_KEY = settings.DJANGOSPAM_COOKIE_KEY
except AttributeError:
    COOKIE_KEY = "dsid"
    
try: # COOKIE_PASS means we don't know if it is a spammer or not.
    COOKIE_PASS = settings.DJANGOSPAM_COOKIE_PASS
except AttributeError:
    COOKIE_PASS = "0"
    
try:
    COOKIE_SPAM = settings.DJANGOSPAM_COOKIE_SPAM
except AttributeError:
    COOKIE_SPAM = "1"

try:
    DISCARD_NO_COOKIE = settings.DJANGOSPAM_DISCARD_NO_COOKIE
except AttributeError:
    DISCARD_NO_COOKIE = False

# Mandatory settings for Akismet:
try:
    AKISMET_KEY = settings.AKISMET_KEY
    AKISMET_USERAGENT = settings.AKISMET_USERAGENT
    AKISMET_USERAGENT_VERSION = settings.AKISMET_USERAGENT_VERSION
    AKISMET_BLOG = settings.AKISMET_BLOG
except AttributeError:
    pass
