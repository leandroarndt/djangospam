djangospam
==========

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

*TODO*

Results
-------

The fake form alone is getting 100% efficiency at
<http://www.correioprogressista.com.br/>, which used to have more than 200
spam comments each day.