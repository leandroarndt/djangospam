# -*- coding: utf-8 -*-
from django.conf import settings

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