# -*- coding: utf-8 -*-
from django.conf.urls import patterns

urlpatterns = patterns("views",
                       r"^/spam$", "spammer_view")