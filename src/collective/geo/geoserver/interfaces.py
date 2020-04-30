from zope import schema
from zope.interface import Interface

from collective.geo.geoserver import geoMessageFactory as _


class IGeoQuery(Interface):
    """ GeoQuery Content interface """


class IGeoServer(Interface):
    """ Geoserver Utility Interface """

    host = schema.TextLine(
        title=_(u"Server"),
        description=_(u"An ip or name"),
        default=u"string:localhost",
        required=True)

    port = schema.TextLine(
        title=_(u"Port"),
        description=_(u"Server Port"),
        default=u"string:9001",
        required=True)

    url_wms = schema.TextLine(
        title=_(u"WMS Path"),
        description=_(u"The wms path, domain excluded"),
        default=u"string:/geoserver/it.geosolutions/wms",
        required=True)

    rest_path = schema.TextLine(
        title=_(u"REST Path"),
        description=_(u"Rest path for queries"),
        default=u"string:/geoserver/rest",
        required=True)

    cformat = schema.TextLine(
        title=_(u"Format"),
        description=_(u"Format of results "),
        default=u"string:application%2Fvnd.google-earth.kml%2Bxml",
        required=True)
