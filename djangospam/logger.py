# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys, os, pwd, datetime
import settings

class LogError(Exception):
    def __init__(self, exc_type, exc_value):
        self.msg = "%s while trying to write log on %s. Is it writeable by %s?\
\nReturned message: \"%s\"." % (
                     exc_type.__name__, settings.DJANGOSPAM_LOG,
                     pwd.getpwuid(os.getuid())[0], exc_value,
                     )
    
    def __str__(self):
        return self.msg

def log(ltype, method, page, user_agent):
    try:
        f = open(settings.DJANGOSPAM_LOG, "a")
        f.write("%s: %s method %s page %s user agent %s\n" % \
                (datetime.datetime.now(), ltype, method, page, user_agent))
        f.close()
    except:
        if settings.DJANGOSPAM_FAIL_ON_LOG:
            exc_type, exc_value = sys.exc_info()[:2]
            raise LogError(exc_type, exc_value)
