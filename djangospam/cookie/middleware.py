# -*- coding: utf-8 -*-
"""Middleware module. See :mod:`djangospam.cookie` for more info."""

from django.http import HttpResponse
from datetime import datetime, timedelta

from djangospam.settings import COOKIE_KEY, COOKIE_PASS, COOKIE_SPAM, \
                                DJANGOSPAM_LOG
from djangospam import logger

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
                if DJANGOSPAM_LOG:
                    logger.log("SPAM REQUEST", request.method,
                       request.path_info,
                       request.META.get("HTTP_USER_AGENT", "undefined"))
                return response
        if DJANGOSPAM_LOG:
            logger.log("PASS REQUEST", request.method, request.path_info,
                       request.META.get("HTTP_USER_AGENT", "undefined"))
        return None
    
    def process_response(self, request, response):
        """Sets "Ok" cookie on unknown users."""
        if COOKIE_KEY not in request.COOKIES:
        # Unknown user, set cookie and go on...
            response.set_cookie(COOKIE_KEY, COOKIE_PASS, httponly=True,
                                expires=datetime.now()+timedelta(days=30))
            # Only logged if we have to set the PASS cookie
            if DJANGOSPAM_LOG:
                logger.log("PASS RESPONSE", request.method, request.path_info,
                           request.META.get("HTTP_USER_AGENT", "undefined"))                
        return response
