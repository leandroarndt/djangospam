# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       (r'^spam$', 'djangospam.cookie.views.spammer_view'),)