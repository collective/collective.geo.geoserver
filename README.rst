Introduction
============

collective.geo.geoserver provides a content type who represent
a layer from Geoserver.

Found a bug? Please, use the `issue tracker`_.

.. contents:: Table of contents

Requirements
============

* `Plone`_ >= 4.1
* `collective.geo.kml`_
* `Geoserver`_

Installation
============

You can install collective.geo.geoserver as part of a specific project's buildout, by having a buildout configuration such as: ::

        [buildout]
        ...
        eggs =
            collective.geo.geoserver
        ...

Install this product from the Plone control panel.

Install Geoserver and run it.

Check plone_properties/geoserver_connector to change Geoserver port or urls.


Contributors
============

* Federico Guizzardi - cippino

.. _Plone: http://plone.org
.. _collective.geo.kml: http://pypi.python.org/pypi/collective.geo.kml
.. _Geoserver: http://geoserver.org/display/GEOS/Welcome
.. _issue tracker: https://github.com/collective/collective.geo.geoserver/issues