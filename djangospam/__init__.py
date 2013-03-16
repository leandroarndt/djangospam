# -*- coding: utf-8 -*-
"""
Django antispam module with an invisible fake comment/contact form and Akismet
verification.

Fake form use
-------------

Include `djangospam` in your installed modules (at `settings.py`) and
insert the following code in your template, **before** the true form::

    {% include 'djangospam/form.html' %}

You may also define a `spam_uri` context variable with the
fake formulary destination URI. If no URI is defined, the form will be posted
at the same address of the page in which the form has been placed
(it will be used a
`<form style="display:none" method="post" action="">...</form>`
code). The destination address must accept POST requests and should not change
the database.

Akismet
-------

Besides including `djangospam` in your installed modules (at `settings.py`),
you should insert the following code to your models file::
    
    from djangospam import akismet
    
    class MyModel(...):
        ...
    
    try:
        akismet.register(MyModel)
    except akismet.AlreadyModerated:
        pass
    
You also **must** define the variables below at `settings.py`:

AKISMET_BLOG
    Your home page URL, including http://
AKISMET_KEY
    Your application key at akismet.com
AKISMET_USERAGENT
    Your application name
AKISMET_USERAGENT_VERSION
    Your application version
DISCARD_SPAM
    If spam should be either automaticaly discarded or marked as not public and
    removed

Results
-------

The fake form alone is getting 100% efficiency at
http://www.correioprogressista.com.br/, which used to have more than 200
spam comments each day. Even so, I recommend using Akismet or another
spam analysis tool."""

__version__ = "0.2.2"