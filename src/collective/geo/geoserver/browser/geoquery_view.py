from Products.Five import BrowserView

from collective.geo.kml.interfaces import IKMLOpenLayersView
from zope.interface import implements

from collective.geo.geoserver.interfaces import IGeoServer
from zope.component import getUtility


class GeoQueryView(BrowserView):
    """GeoQuery default view """

    implements(IKMLOpenLayersView)


class KMLDocument(BrowserView):
    def __call__(self):
        ut = getUtility(IGeoServer)

        self.request.response.setHeader(
            'Content-Type', '%s;charset=utf-8' % ut.getFormat()
        )
        return ut.getMap(self.context.getLayer(),
                         self.context.getSrid(),
                         self.context.getCqlfilter())
