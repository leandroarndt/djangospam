# -*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime, timedelta

from cookie import COOKIE_KEY, COOKIE_OK, COOKIE_SPAM

class SpamCookieMiddleware(object):
    """Verifies if a client has already been tagged as spam bot through
`djangospam/cookie.html`. You should add
`djangospam.cookie.SpamCookieMiddleware` to your `MIDDLEWARE CLASSES` at
`settings.py`."""

    def process_request(self, request):
        """Discovers if a request is from a knwon spam bot and denies access."""
        
        if COOKIE_KEY in request.COOKIES and \
            request.get_cookie(COOKIE_KEY) == COOKIE_SPAM:
                # Is a known spammer.
                response = HttpResponse("")
                # We do not reveal why it has been forbbiden:
                response.status_code = 404
                return response
        return None
    
    def process_response(self, request, response):
        """Sets "Ok" cookie on unknown users."""
        if COOKIE_KEY not in request.COOKIES:
        # Unknown user, set cookie and go on...
            response.set_cookie(COOKIE_KEY, COOKIE_OK, httponly=True,
                                expires=datetime.now()+timedelta(days=30))
        return response
