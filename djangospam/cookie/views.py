# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, Template
from datetime import datetime, timedelta

from djangospam.settings import COOKIE_KEY, COOKIE_SPAM, DJANGOSPAM_LOG
from djangospam.logger import log

def spammer_view(request):
    """View for setting cookies on spammers."""

    # Permits use of CSRF middleware
    context = RequestContext(request, {})
    template = Template("")

    response = HttpResponse(template.render(context))
    # Sets a cookie with a 10 years lifetime, accessible only via HTTP:
    response.set_cookie(COOKIE_KEY, value=COOKIE_SPAM, httponly=True,
                        expires=datetime.now()+timedelta(days=3650))
    
    if DJANGOSPAM_LOG:
        log("BLOCK RESPONSE", request.method, request.path_info,
            request.META.get("HTTP_USER_AGENT", "undefined"))

    return response