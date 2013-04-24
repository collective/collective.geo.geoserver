from zope import schema
from zope.interface import Interface


class IGeoQuery(Interface):
    """ GeoQuery Content interface """


class IGeoServer(Interface):
    """ Geoserver Utility Interface """

    host = schema.TextLine(
        title=u"Server",
        description=u"An ip or name",
        default=u"string:localhost",
        required=True)

    port = schema.TextLine(
        title=u"Port",
        description=u"Server Port",
        default=u"string:9001",
        required=True)

    url_wms = schema.TextLine(
        title=u"WMS Path",
        description=u"The wms path, domain excluded",
        default=u"string:/geoserver/it.geosolutions/wms",
        required=True)

    rest_path = schema.TextLine(
        title=u"REST Path",
        description=u"Rest path for queries",
        default=u"string:/geoserver/rest",
        required=True)

    cformat = schema.TextLine(
        title=u"Format",
        description=u"Format of results ",
        default=u"string:application%2Fvnd.google-earth.kml%2Bxml",
        required=True)
