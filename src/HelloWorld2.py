import rdflib
from rdflib import plugin


plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')

#Get a Graph object
g = rdflib.Graph()
# pull in an RDF document from NeuroLex, parse, and store.
#result = g.parse("http://neurolex.org/wiki/Special:ExportRDF/birnlex_1489", format="application/rdf+xml")
#result = g.parse("/Users/ryansoscia/BAMS-to-NeuroLex/Data/bams_ontology_2013-07-10_03-20-00.xml", format="application/rdf+xml")

result = g.parse("http://neurolex.org/wiki/Special:ExportRDF/birnlex_1489", format="application/rdf+xml")


#Ask a specific question about that RDF document

qres = g.query(
    """SELECT DISTINCT ?x
       WHERE {
          ?a property:Definition "birnlex_1489"^^xsd:string ?x.
    	}""",
    initNs=dict(
        property=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/birnlex_1489"),
        wiki=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/")))


#troubleshooting the problem.. trying to find the root
#print("root is %s" % root[qres.result[:0]])
#initBindings={'x' : wiki}


#Gives the first property
print("Definition: %s" % qres.result[0])