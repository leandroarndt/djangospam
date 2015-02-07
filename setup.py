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
    description = "Django antispam module with invisible fake comment/contact\
 form, cookie based middleware and Akismet verification.",
    author = "Leandro Arndt",
    author_email = "contato@caritasinveritate.teo.br",
    url = "https://github.com/leandroarndt/djangospam",
    download_url = \
        "https://github.com/leandroarndt/djangospam/archive/v"+\
        djangospam.__version__+".tar.gz",
    keywords = ["django", "spam", "akismet", "middleware"],
    requires = ["django"],
    license = "BSD",
    platforms = "OS independent",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
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

Django antispam module aimed at Django with an invisible fake comment/contact form,
cookie based middleware and Akismet verification.

See http://pythonhosted.org/djangospam for complete documentation. Djangospam
is compatible with both Python 2 and 3.

See https://github.com/leandroarndt/djangospam for development versions.

Quick start
-----------

These are the basic steps for using djangospam. You can get more info on
the cited modules and at `djangospam.settings`.

Fake form with cookie middleware
++++++++++++++++++++++++++++++++

*New in version 0.3.0*

The cookie middleware uses cookies to identify known spam bots. Simple
crawlers usually don't accept cookies, but spam bots may accept, since
a website may require this to receive comments. In order to use the
cookie middleware, add `djangospam.cookie.middleware.SpamCookieMiddleware`
to `MIDDLEWARE_CLASSES` at your settings file (usually `settings.py`).
In your template, insert **before** the true form::
    
    {% include 'djangospam/cookieform.html' %}

You must also add `(r"^somewhere/", include("djangospam.cookie.urls")`
to your url patterns (usually in your root urls.conf; `somewhere`
may be any path, except the one used for true posts).
I suggest using the following paths::
    
    (r'^comments/', include('djangospam.cookie.urls')),
    (r'^spam/', include('django_comments.urls')),

Fake form without middleware
++++++++++++++++++++++++++++

You may also use the fake form without the cookie middleware. This will
*not* block access from known spam bots. In order to do this,
include `djangospam` in your installed modules (at `settings.py`) and
insert the following code in your template, **before** the true form::

    {% include 'djangospam/form.html' %}

You may also define a `spam_uri` context variable with the
fake formulary destination URI. If no URI is defined, the form will be posted
at the same address of the page in which the form has been placed
(it will be used a
`<form method="post" action="">...</form>`
code). The destination address must accept POST requests and should not change
the database.

You may customize the fake formulary by copying it's template to
`template/djangospam` at your application's directory and editing it.

Cookie-based moderator
++++++++++++++++++++++

*New in version 0.4.0*

`djangospam.cookie.moderator` defines a cookie-based comment moderator
that should be attached to
your commented model. This moderator tests comment post requests for
the djangospam cookie and discards those which don't have it.
See `djangospam.cookie.middleware` for more info on the cookie system.
Code that uses this comment moderator **must** use that middleware.

Your models file should be like this::
    
    from djangospam.cookie import moderator as cookie
    
    class MyModel(...):
        ...
    
    try:
        cookie.register(MyModel)
    except cookie.AlreadyModerated:
        pass

Akismet
+++++++

*New in version 0.2.0*

`djangospam.akismet.moderator` defines an Akismet-based comment moderator.
Besides including `djangospam` in your installed modules (at `settings.py`),
you should insert the following code to your models file::
    
    from djangospam.akismet import moderator as akismet
    
    class MyModel(...):
        ...
    
    try:
        akismet.register(MyModel)
    except akismet.AlreadyModerated:
        pass

**Warning:**
    Since version 0.4.0, the Akismet moderator has been turned a separate
    subpackage. Code using it must be rewritten as follows::
        
        from djangospam import akismet
        
    must be changed to::
        
        from djangospam.akismet import moderator as akismet
    
    Using from `djangospam import akismet` is now deprecated and won't be
    available from 1.0.0 on.
    
You also **must** define the variables below at `settings.py`:

AKISMET_BLOG
    Your home page URL, including http://
AKISMET_KEY
    Your application key at akismet.com
AKISMET_USERAGENT
    Your application name
AKISMET_USERAGENT_VERSION
    Your application version

Results
=======

Since version 0.4.3, the cookie-based middleware (with fake forms and
the cookie-based comment moderator) has achieved 100% efficiency at former
http://www.correioprogressista.com.br/, which used to have more than 200
spam comments each day. Even so, I recommend using Akismet or another
spam analysis tool.

Since version 0.3.0 (first with cookie middleware) up to 8th april 2013,
the cookie middleware identified 5166 spammers and blocked 1917 requests
from known spammers at the same website::

     $ grep -c "BLOCK RESPONSE" spam.log 
    5166
     $ grep -c "SPAM REQUEST" spam.log 
    1917

Change log
==========

* 1.1:
    * 1.1.2 (*2015-02-07*):
        * Tries to import django_comments before django.comments.moderator.
    * 1.1.1 (*2015-02-05*):
        * Fixed Windows compatibility issue on logger.
    * 1.1.0 (*2015-02-05*):
        * Added support for django_comments (former django.contrib.comments)
* 1.0:
    * 1.0.1 (*2015-01-10*):
        * Added support for Django 1.4 and later.
    * 1.0.0 (*2013-04-01*):
        * Changed version number and labeled as "stable".
* 0.4:
    * 0.4.3 (*2013-03-23*):
        * Fake forms made invisible via javascript.
    * 0.4.2 (*2013-03-22*):
        * Akismet settings made optional for non-Akismet users.
    * 0.4.1 (*2013-03-21*):
        * Bugfix at djangospam.akismet.
    * 0.4.0 (*2013-03-20*):
        * Added cookie-based comment moderator.
        * Transformed Akismet module into a separate subpackage.
            **Warning:**
            Code that used Akismet module needs to be rewritten. See
            `djangospam.akismet` for the current code. Old code should
            work until 1.0.0.
        * Improved logger.
* 0.3:
    * 0.3.4 (*2013-03-18*):
        * Improved forms and URL.
    * 0.3.3 (*2013-03-17*):
        * Worked around pip bug.
    * 0.3.2 (*2013-03-17*):
        * Fixed new setup bug (setup.py) - NOT A BUG, see v. 0.3.3.
    * 0.3.1 (*2013-03-17*):
        * Fixed setup bug (in Manifest.in)
    * 0.3.0 (*2013-03-17*):
        * Implemented cookie middleware
* 0.2:
    * 0.2.2 (*2013-03-16*):
        * Fixed bug at akismet module.
    * 0.2.1 (*2013-03-13*):
        * Made compatible with both Python 2 and 3.
    * 0.2.0 (*2013-03-10*):
        * Implemented Akismet verification.
* 0.1:
    * 0.1.1-0.1.6 (*2013-03-10*):
        * Bugfixes.
    * 0.1.0 (*2013-03-09*):
        * First version.

""",
)
