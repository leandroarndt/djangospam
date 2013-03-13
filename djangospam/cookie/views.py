# -*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime, timedelta

from cookie import COOKIE_KEY, COOKIE_SPAM

def spammerView(request):
    """View for setting cookies on spammers. Used in conjunction with
    spamform_ tag."""
    response = HttpResponse("")
    # Sets a cookie with a 10 years lifetime, accessible only via HTTP:
    response.set_cookie(COOKIE_KEY, value=COOKIE_SPAM, httponly=True,
                        expires=datetime.now()+timedelta(days=3650))
    return response()