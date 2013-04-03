from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory

from collective.geo.geoserver.interfaces import IGeoServer
from zope.component import getUtility

class baseVocabulary(object):
    implements(IVocabularyFactory)
    terms = []

    def __call__(self, context):
        terms = []
        for v in self.terms:
            terms.append(SimpleVocabulary.createTerm(v,v,v))
        return SimpleVocabulary(terms)

class layers_vocabulary(baseVocabulary):
    @property
    def terms(self):
        ut=getUtility(IGeoServer)
        return ut.getLayers()

class srid_vocabulary(baseVocabulary):
    @property
    def terms(self):
        ut=getUtility(IGeoServer)
        return ut.getSRid()


        