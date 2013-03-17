# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, Template
from datetime import datetime, timedelta

from settings import COOKIE_KEY, COOKIE_SPAM, COOKIE_LOG

def spammer_view(request):
    """View for setting cookies on spammers."""

    # Permits use of CSRF middleware
    context = RequestContext(request, {})
    template = Template("")

    response = HttpResponse(template.render(context))
    # Sets a cookie with a 10 years lifetime, accessible only via HTTP:
    response.set_cookie(COOKIE_KEY, value=COOKIE_SPAM, httponly=True,
                        expires=datetime.now()+timedelta(days=3650))
    
    if COOKIE_LOG:
        f = open(COOKIE_LOG, "a")
        f.write("BLOCK RESPONSE type %s page %s user agent %s\n" %\
                (request.method, request.path_info,
                 request.META["HTTP_USER_AGENT"]))
        f.close()

    return response