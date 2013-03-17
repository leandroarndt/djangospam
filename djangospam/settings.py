# -*- coding: utf-8 -*-
from django.conf import settings

# Optional settings:
try:
    DISCARD_SPAM = settings.DISCARD_SPAM
except AttributeError:
    DISCARD_SPAM = False

# Mandatory settings:
AKISMET_KEY = settings.AKISMET_KEY
AKISMET_USERAGENT = settings.AKISMET_USERAGENT
AKISMET_USERAGENT_VERSION = settings.AKISMET_USERAGENT_VERSION
AKISMET_BLOG = settings.AKISMET_BLOG