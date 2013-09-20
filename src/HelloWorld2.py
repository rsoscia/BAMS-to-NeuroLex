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
result = g.parse("http://neurolex.org/wiki/Special:ExportRDF/birnlex_1489", format="application/rdf+xml")

#Ask a specific question about that RDF document

qres = g.query(
    """SELECT DISTINCT ?x ?axonl
       WHERE {
          ?x property:Id "nifext_128"^^xsd:string . ?x property:AxonLength ?axonl
    	}""",
    initNs=dict(
        property=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/nifext_128"),
        wiki=rdflib.Namespace("http://neurolex.org/wiki/Special:URIResolver/")))


#Gives the first property
print("Definition: %s" % qres.result[0])
#says the index is out of range

#Gives every property
print("Definition: %s" % qres.result[:0])



