# -*- coding: utf-8 -*-
"""Provides general options and akismet settings.

General options
---------------

This option is used by more than one djangospam module/package:

DISCARD_SPAM
    If spam should be either automaticaly discarded or marked as not public and
    removed. Defaults to `False`.

Logging settings
----------------

These afect :mod:`djangospam.logger`:

DJANGOSPAM_COOKIE_LOG
    Log file path and name. Defaults to `False` (no logging).
DJANGOSPAM_FAIL_ON_LOG
    If djangospam should raise an exception when it fails to log. Defaults
    to `False`.
    
Akismet settings
----------------

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
    DJANGOSPAM_FAIL_ON_LOG = settings.DJANGOSPAM_FAIL_ON_LOG
except AttributeError:
    DJANGOSPAM_FAIL_ON_LOG = False

# Mandatory settings:
AKISMET_KEY = settings.AKISMET_KEY
AKISMET_USERAGENT = settings.AKISMET_USERAGENT
AKISMET_USERAGENT_VERSION = settings.AKISMET_USERAGENT_VERSION
AKISMET_BLOG = settings.AKISMET_BLOG