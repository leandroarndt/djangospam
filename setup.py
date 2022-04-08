# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
version = '1.1.5'

setuptools.setup(
    name= "djangospam",
    packages = setuptools.find_packages(),
    package_data = {"djangospam": ["templates/djangospam/form.html",
                                   "templates/djangospam/cookieform.html"]},
    version = version,
    description = "Django antispam module with invisible fake comment/contact\
    form, cookie based middleware and Akismet verification.",
    author = "Leandro Arndt",
    author_email = "contato@caritasinveritate.teo.br",
    url = "https://github.com/leandroarndt/djangospam",
    project_urls={
        'Bug tracker': 'https://github.com/leandroarndt/djangospam/issues',
    },
    download_url = \
        "https://github.com/leandroarndt/djangospam/archive/v"+\
        version+".tar.gz",
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
    long_description = long_description,
    long_description_content_type="text/markdown",
)
