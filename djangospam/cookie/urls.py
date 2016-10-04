# -*- coding: utf-8 -*-
"""URL for setting SPAM value to the `djangospam.cookie` cookie.
You must also add `(r"^somewhere/", include("djangospam.cookie.urls")`
to your url patterns (usually in your root urls.conf; `somewhere`
may be any path, except the one used for true posts).
"""

try:
    from django.conf.urls import patterns, url
except ImportError:
    try:
        from django.conf.urls.defaults import patterns, url
    except ImportError:
        from django.conf.urls import url

from .views import spammer_view

try:
    urlpatterns = patterns('',
                        url(r'^post$', 'djangospam.cookie.views.spammer_view', name='spammer_view'),)
except NameError:
    urlpatterns = [url(r'^post$', spammer_view, name='spammer_view'),]