# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name= "djangospam",
    packages = ["djangospam"],
    version = "0.1",
    description = "Django antispam module",
    author = "Leandro Arndt",
    author_email = "contato@correioprogressista.com.br",
    url = "https://github.com/leandroarndt/djangospam",
    download_url = \
        "https://github.com/leandroarndt/djangospam/archive/master.zip",
    keywords = ["django", "spam", "akismet"],
    requires = ["django"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    long_description = """
djangospam
==========

Django antispam module with an invisible fake comment/contact form and Akismet
verification.

Fake form use
-------------

Include `djangospam.spam` in your installed modules (at `settings.py`) and
insert the following code in your template (*todo*)::

    {% load spam %}
    
    ...
    
    {% spam 'optional destination uri' }

or (*working*)::

    {% include 'spam/form.html' %}

In this last case, you may also define a `spam_uri` context variable with the
fake formulary destination URI. If no URI is defined, the form will be posted
at the same address of the page being attacked
(It will be used a `<form method="post" action="">...</form>` code).

Akismet
-------

*TODO*

Results
-------

The fake form alone is getting 100% efficiency at
<http://www.correioprogressista.com.br/>, which used to have more than 200
spam comments each day. Even so, I recommend using Akismet or another
spam analysis tool.""",
)