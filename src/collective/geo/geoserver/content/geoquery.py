""" Definition of the GeoQuery content types
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema

from collective.geo.geoserver import geoMessageFactory as _
from collective.geo.geoserver.config import PROJECTNAME
from collective.geo.geoserver.interfaces import IGeoQuery

from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName

GeoQuerySchema = ATContentTypeSchema.copy()+atapi.Schema((
    atapi.StringField('layer',
        required=True,
        searchable=False,
        vocabulary_factory='layers_vocabulary',
        widget=atapi.SelectionWidget(
            label=_(u'label_layer',default='Layer'),
            description=_(u'help_layer',default=u'Select a layer from the list.'),
        ),
    ),

    atapi.StringField('srid',
        required=True,
        searchable=False,
        default='EPSG:4326',
        vocabulary_factory='srid_vocabulary',
        widget=atapi.SelectionWidget(
            label=_(u'label_srid',default='SRID'),
            description=_(u'help_srid',default=u'Spatial Reference Identifier: usually EPGS:4326 (WGS84)'),
        ),
    ),
        
    atapi.TextField('cqlfilter',
        required=False,
        searchable=False,
        defaunt='',
        default_content_type = 'text/plain',
        default_output_type = 'text/plain',
        allowable_content_types=['text/plain',],
        widget=atapi.TextAreaWidget(
            label=_(u'label_cql_filter',default='CQL Filter'),
            description=_(u'help_cql_filter',default=u'CQL filter for maps information.'),
        ),
    ),
      
))

GeoQuerySchema['title'].storage=atapi.AnnotationStorage()
GeoQuerySchema['description'].storage=atapi.AnnotationStorage()
schemata.finalizeATCTSchema(GeoQuerySchema, moveDiscussion=False)

class GeoQuery(ATCTContent):
    """ GeoQuery Content Type """
    implements(IGeoQuery)
    schema=GeoQuerySchema
    meta_type=portal_type="GeoQuery"

    security = ClassSecurityInfo()
 
atapi.registerType(GeoQuery,PROJECTNAME)
