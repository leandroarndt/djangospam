# -*- coding: utf-8 -*-
"""URL for setting SPAM value to the `djangospam.cookie` cookie.
You must also add `(r"^somewhere/", include("djangospam.cookie.urls")`
to your url patterns (usually in your root urls.conf; `somewhere`
may be any path).
"""

from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       (r'^post$', 'djangospam.cookie.views.spammer_view'),)