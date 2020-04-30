Introduction
============

``collective.geo.geoserver`` provides a content type who represent
a layer from Geoserver.

.. contents:: Table of contents


Requirements
============

* `Plone`_ >= 4.1
* `collective.geo.kml`_
* `Geoserver`_


Documentation
=============

Full documentation for end users can be found in the "docs" folder.
It is also available online at https://collectivegeo.readthedocs.io/


Translations
============

This product has been translated into

- Spanish.

- Italian.

You can contribute for any message missing or other new languages, join us at 
`Plone Collective Team <https://www.transifex.com/plone/plone-collective/>`_ 
into *Transifex.net* service with all world Plone translators community.


Installation
============

You can install ``collective.geo.geoserver`` as part of a specific project's buildout, 
by having a buildout configuration such as: ::

        [buildout]
        ...
        eggs =
            collective.geo.geoserver
        ...

Install this product from the Plone control panel.

Install Geoserver and run it.

Check ``plone_properties/geoserver_connector`` to change Geoserver port or urls.


Tests status
============

This add-on is tested using Travis CI. The current status of the add-on is:

.. image:: https://img.shields.io/travis/collective/collective.geo.geoserver/master.svg
    :target: https://travis-ci.org/collective/collective.geo.geoserver

.. image:: http://img.shields.io/pypi/v/collective.geo.geoserver.svg
   :target: https://pypi.org/project/collective.geo.geoserver


Contribute
==========

Have an idea? Found a bug? Let us know by `issue tracker`_.

- Issue Tracker: https://github.com/collective/collective.geo.geoserver/issues
- Source Code: https://github.com/collective/collective.geo.geoserver
- Documentation: https://collectivegeo.readthedocs.io/


Contributors
============

* Federico Guizzardi - cippino
* Leonardo J. Caballero G. - macagua


License
=======

The project is licensed under the GPLv2.

.. _Plone: https://plone.org/
.. _collective.geo.kml: https://pypi.org/project/collective.geo.kml
.. _Geoserver: http://geoserver.org/display/GEOS/Welcome
.. _issue tracker: https://github.com/collective/collective.geo.geoserver/issues
