# -*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime, timedelta

from settings import COOKIE_KEY, COOKIE_PASS, COOKIE_SPAM, COOKIE_LOG

class SpamCookieMiddleware(object):
    """Verifies if a client has already been tagged as spam bot through
`djangospam/cookieform.html`. You should add
`djangospam.cookie.SpamCookieMiddleware` to your `MIDDLEWARE CLASSES` at
`settings.py`. See :mod:`djangospam.cookie` for additional help."""

    def process_request(self, request):
        """Discovers if a request is from a knwon spam bot and denies access."""
        
        if COOKIE_KEY in request.COOKIES and \
            request.COOKIES[COOKIE_KEY] == COOKIE_SPAM:
                # Is a known spammer.
                response = HttpResponse("")
                # We do not reveal why it has been forbbiden:
                response.status_code = 404
                if COOKIE_LOG:
                    f = open(COOKIE_LOG, "a")
                    f.write("SPAM REQUEST type %s page %s user agent %s\n" %\
                            (request.method, request.path_info,
                             request.META["HTTP_USER_AGENT"]))
                    f.close()
                return response
        if COOKIE_LOG:
            f = open(COOKIE_LOG, "a")
            f.write("PASS REQUEST type %s page %s user agent %s\n" %\
                    (request.method, request.path_info,
                     request.META["HTTP_USER_AGENT"]))
            f.close()
        return None
    
    def process_response(self, request, response):
        """Sets "Ok" cookie on unknown users."""
        if COOKIE_KEY not in request.COOKIES:
        # Unknown user, set cookie and go on...
            response.set_cookie(COOKIE_KEY, COOKIE_PASS, httponly=True,
                                expires=datetime.now()+timedelta(days=30))
            # Only logged if we have to set the PASS cookie
            if COOKIE_LOG:
                f = open(COOKIE_LOG, "a")
                f.write("PASS RESPONSE type %s page %s user agent %s\n" %\
                        (request.method, request.path_info,
                         request.META["HTTP_USER_AGENT"]))
                f.close()
                
        return response
