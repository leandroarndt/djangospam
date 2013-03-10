# -*- coding: utf-8 -*-
from distutils.core import setup
import djangospam

setup(
    name= "djangospam",
    packages = ["djangospam"],
    package_data = {"djangospam": ["templates/djangospam/form.html"]},
    version = djangospam.__version__,
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

See <https://github.com/leandroarndt/djangospam> for up to date help.

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

*TODO*

Results
-------

The fake form alone is getting 100% efficiency at
<http://www.correioprogressista.com.br/>, which used to have more than 200
spam comments each day. Even so, I recommend using Akismet or another
spam analysis tool.""",
)