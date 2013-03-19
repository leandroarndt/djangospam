# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys, os, pwd
import settings

class LogError(Exception):
    def __init__(self, exc_type, exc_value):
        self.msg = "%s while trying to write log on %s. Is it writeable by %s?\
 Returned message: \"%s\"." % (
                     exc_type, exc_value, settings.COOKIE_LOG,
                     pwd.getpwuid(os.getuid())[0], exc_value,
                     )

def log(ltype, method, page, user_agent):
    try:
        f = open(settings.COOKIE_LOG, "a")
        f.write("%s method %s page %s user agent %s\n" % \
                (ltype, method, page, user_agent))
        f.close()
    except:
        if settings.DJANGOSPAM_FAIL_ON_LOG:
            raise LogError(sys.exc_info()[:2])
