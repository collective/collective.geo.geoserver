from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.geo.geoserver


COLLECTIVE_GEO_GEOSERVER = PloneWithPackageLayer(
    zcml_package=collective.geo.geoserver,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.geo.geoserver:testing',
    name="COLLECTIVE_GEO_GEOSERVER")

COLLECTIVE_GEO_GEOSERVER_INTEGRATION = IntegrationTesting(
    bases=(COLLECTIVE_GEO_GEOSERVER, ),
    name="COLLECTIVE_GEO_GEOSERVER_INTEGRATION")

COLLECTIVE_GEO_GEOSERVER_FUNCTIONAL = FunctionalTesting(
    bases=(COLLECTIVE_GEO_GEOSERVER, ),
    name="COLLECTIVE_GEO_GEOSERVER_FUNCTIONAL")
