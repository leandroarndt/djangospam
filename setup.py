# -*- coding: utf-8 -*-
from distutils.core import setup
import setuptools
import djangospam

setup(
    name= "djangospam",
    packages = setuptools.find_packages(),
    package_data = {"djangospam": ["templates/djangospam/form.html",
                                   "templates/djangospam/cookieform.html"]},
    version = djangospam.__version__,
    description = "Django antispam module",
    author = "Leandro Arndt",
    author_email = "contato@correioprogressista.com.br",
    url = "https://github.com/leandroarndt/djangospam",
    download_url = \
        "https://github.com/leandroarndt/djangospam/archive/v0.3.2.tar.gz",
    keywords = ["django", "spam", "akismet", "middleware"],
    requires = ["django"],
    license = "BSD",
    platforms = "OS independent",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    long_description = """
djangospam
==========

Django antispam module with an invisible fake comment/contact form,
cookie based middleware and Akismet verification.

See http://pythonhosted.org/djangospam for complete documentation. Djangospam
is compatible with both Python 2 and 3.

General options
---------------

These options are used by more than one djangospam module/package:

DISCARD_SPAM
    If spam should be either automaticaly discarded or marked as not public and
    removed.
DJANGOSPAM_COOKIE_LOG
    Log file path and name. Defaults to `False` (no logging).

Fake form with cookie middleware
--------------------------------

*New in version 0.3.0*

The cookie middleware uses cookies to identify known spam bots. Simple
crawlers usually don't accept cookies, but spam bots may accept, since
a website may require this to receive comments. In order to use the
cookie middleware, add `djangospam.cookie.middleware.SpamCookieMiddleware`
to `MIDDLEWARE_CLASSES` at your settins file (usually `settings.py`).
In your template, insert::
    
    {% include 'djangospam/cookieform.html' %}

You may also define some variables at your settings file to customize
your cookie:

DJANGOSPAM_COOKIE_KEY
    The cookie identifier. Defaults to `dsid`.
DJANGOSPAM_COOKIE_PASS
    The initial value of the cookie. It is used only to know beforehand if
    the user agent accepts cookies. Defaults to `0`.
DJANGOSPAM_COOKIE_SPAM
    The cookie value for known spammers. If the HTTP request presents
    djangospam cookie with this value, the middleware will return a 404
    status code (moved permanently or forbidden, according to the standards).
    Defaults to `1`.
    
**Note:** If `djangospam.cookie.middleware.SpamCookieMiddleware`
is being used, `djangospam.akismet` module
will treat as spam any comment attempt with cookies disabled.

You may customize the fake formulary by copying it's template to
`template/djangospam` at your application's directory and editing it.

Fake form without middleware
----------------------------

You may also use the fake form without the cookie middleware. This will
*not* block access from known spam bots. In order to do this,
include `djangospam` in your installed modules (at `settings.py`) and
insert the following code in your template, **before** the true form::

    {% include 'djangospam/form.html' %}

You may define a `spam_uri` context variable with the
fake formulary destination URI. If no URI is defined, the form will be posted
at the same address of the page in which the form has been placed
(it will be used a
`<form method="post" action="">...</form>`
code). The destination address must accept POST requests and should not change
the database.

You may customize the fake formulary by copying it's template to
`template/djangospam` at your application's directory and editing it.

Akismet
-------

*New in version 0.2.0*

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
    
**Note:** If `djangospam.cookie.middleware.SpamCookieMiddleware`
is being used, `djangospam.akismet` module
will treat as spam any comment attempt with cookies disabled.

Results
-------

The fake form alone is getting more than 99,9% (*circa* 1,399 out of 
1,400 spam comments) efficiency at
http://www.correioprogressista.com.br/, which used to have more than 200
spam comments each day. Even so, I recommend using Akismet or another
spam analysis tool.

On the first 14 hours of the cookie middleware at the same website,
it identified 244 spammers and blocked 68 requests from known spammers::
    
    $ grep -c "BLOCK RESPONSE" spam.log 
    244
    $ grep -c "SPAM REQUEST" spam.log 
    68

Change log
----------

* 0.3:
    * 0.3.4 (*2013-03-18*):
        Improved forms and URL.
    * 0.3.3 (*2013-03-17*):
        Worked around pip bug.
    * 0.3.2 (*2013-03-17*):
        Fixed new setup bug (setup.py) - NOT A BUG, see v. 0.3.3.
    * 0.3.1 (*2013-03-17*):
        Fixed setup bug (in Manifest.in)
    * 0.3.0 (*2013-03-17*):
        Implemented cookie middleware
* 0.2:
    * 0.2.2 (*2013-03-16*):
        Fixed bug at akismet module.
    * 0.2.1 (*2013-03-13*):
        Made compatible with both Python 2 and 3.
    * 0.2.0 (*2013-03-10*):
        Implemented Akismet verification.
* 0.1:
    * 0.1.1-0.1.6 (*2013-03-10*):
        Bugfixes.
    * 0.1.0 (*2013-03-09*):
        First version.
""",
)
