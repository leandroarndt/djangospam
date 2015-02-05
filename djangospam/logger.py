# -*- coding: utf-8 -*-
"""Logger for djangospam HTTP events.

Settings
++++++++

DJANGOSPAM_LOG
    Log file path and name. Defaults to `False` (no logging).
DJANGOSPAM_FAIL_ON_LOG
    If djangospam should raise an exception when it fails to log. Defaults
    to `False`.
"""
from __future__ import unicode_literals

import sys, os, datetime

try:
    import pwd
    unix = True
except ImportError:
    unix = False

from djangospam import settings

class LogError(Exception):
    """Exception raised if writing to DJANGOSPAM_LOG fails. Tells which
exception has been raised before."""
    
    def __init__(self, exc_type, exc_value):
        if unix:
            self.msg = "%s while trying to write log on %s. Is it writeable by %s?\
\nReturned message: \"%s\"." % (
                         exc_type.__name__, settings.DJANGOSPAM_LOG,
                         pwd.getpwuid(os.getuid())[0], exc_value,
                         )
        else:
            self.msg = "%s while trying to write log on %s. Is it writeable?\
\nReturned message: \"%s\"." % (
                         exc_type.__name__, settings.DJANGOSPAM_LOG,
                         exc_value,
                         )
    
    def __str__(self):
        return self.msg

def log(ltype, method, page, user_agent):
    """Writes to the log a message in the following format::
        
        "<datetime>: <exception> method <HTTP method> page <path> \
user agent <user_agent>"
                
"""

    try:
        f = open(settings.DJANGOSPAM_LOG, "a")
        f.write("%s: %s method %s page %s user agent %s\n" % \
                (datetime.datetime.now(), ltype, method, page, user_agent))
        f.close()
    except:
        if settings.DJANGOSPAM_FAIL_ON_LOG:
            exc_type, exc_value = sys.exc_info()[:2]
            raise LogError(exc_type, exc_value)
