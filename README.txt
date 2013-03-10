djangospam
==========

Django antispam module with an invisible fake comment/contact form and Akismet
verification.

Fake form use
-------------

Include `djangospam` in your installed modules (at `settings.py`) and
insert the following code in your template (*todo*)::

    {% load djangospam %}
    
    ...
    
    {% djangospam 'optional destination uri' }

or (*working*)::

    {% include 'djangospam/form.html' %}

In this last case, you may also define a `spam_uri` context variable with the
fake formulary destination URI. If no URI is defined, the form will be posted
at the same address of the page being attacked
(It will be used a
`<form style="display:none" method="post" action="">...</form>`
code).

Akismet
-------

*TODO*

Results
-------

The fake form alone is getting 100% efficiency at
<http://www.correioprogressista.com.br/>, which used to have more than 200
spam comments each day.