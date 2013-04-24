from collective.geo.geoserver.interfaces import IGeoServer

from zope.interface import implements

import urllib2

from Products.CMFCore.utils import getToolByName

from plone.memoize import forever
try:
    from zope.app.component.hooks import getSite
except:
    from zope.component.hooks import getSite

from BeautifulSoup import BeautifulSoup

class GeoServer(object):
    implements(IGeoServer)

    @forever.memoize
    def _getProperties(self):
        pt=getToolByName(getSite(),'portal_properties')
        return getattr(pt,'geoserver_connector',None)

    def _getProperty(self,key,default=None):
        val=default
        pp=self._getProperties()
        if pp is not None:
            val=pp.getProperty(key,val)
        return val

    def getHost(self):
        return self._getProperty('host','localhost')

    def getPort(self):
        return self._getProperty('port','9001')

    def getFormat(self):
        return self._getProperty('format','application%2Fvnd.google-earth.kml%2Bxml')

    def _getWMSPath(self,name):
        return self._getProperty('wms_path','/geoserver/%s/wms')%name

    def _getOWSPath(self):
        return self._getProperty('ows_path','/geoserver/ows')

    def _getQueryCapabilities(self):
        return self._getProperty('query_capabilities',('service=wms','version=1.3.0','request=GetCapabilities'))

    def _makeCall(self,url):
        conn=urllib2.urlopen(url)
        return conn.read()

    def getMap(self,layer=None,srid=None,cql_filter=''):
        ws,ly=layer.split(':')
        query=dict(bbox="-90,-90,90,90",
                   request="GetMap",
                   format=self.getFormat(),
                   layers=ly,
                   srs=srid,
                   width=1,
                   height=1,)
        if len(cql_filter)>0:
            query['cql_filter']=cql_filter
        host=self.getHost()
        port=self.getPort()
        path_query=self._getWMSPath(ws)

        qrystr='&'.join(['%s=%s'%item for item in query.items()])

        url="http://%s:%s%s?%s" % (host,port,path_query,qrystr)

        return self._makeCall(url)

    def getLayers(self):
        host=self.getHost()
        port=self.getPort()
        path_query=self._getOWSPath()
        qrystr='&'.join(self._getQueryCapabilities())

        url='http://%s:%s%s?%s'%(host,port,path_query,qrystr)
        content=self._makeCall(url)
        parser=BeautifulSoup(content)
        return [i.find('name').text for i in parser.findAll('layer',queryable="1")]

    def getSRid(self):
        host=self.getHost()
        port=self.getPort()
        path_query=self._getOWSPath()
        qrystr='&'.join(self._getQueryCapabilities())

        url='http://%s:%s%s?%s'%(host,port,path_query,qrystr)
        content=self._makeCall(url)
        parser=BeautifulSoup(content)
        return [i.text for i in parser.wms_capabilities.capability.layer.findAll('crs')]


        

        
