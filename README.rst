ftw.addressblock
################

This Plone add-on installs a new content type which can be used to display
address data. It requires ``ftw.simplelayout``.

Extras
======

There is an extra ``geo`` which installs optional geo and map support. If you
want to use this feature you must install both the ``default`` and the ``geo``
profile in your policy (the  ``geo`` profile won't install the  ``default``
profile).


Development
===========

**Python:**

1. Fork this repo
2. Clone your fork
3. Shell: ``ln -s development.cfg buildout.cfg``
4. Shell: ``python boostrap.py``
5. Shell: ``bin/buildout``

Run ``bin/test`` to test your changes.

Or start an instance by running ``bin/instance fg``.


Links
=====

- GitHub: https://github.com/4teamwork/ftw.addressblock
- Issues: https://github.com/4teamwork/ftw.addressblock/issues
- PyPI: http://pypi.python.org/pypi/ftw.addressblock
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.addressblock


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.addressblock`` is licensed under GNU General Public License, version 2.
